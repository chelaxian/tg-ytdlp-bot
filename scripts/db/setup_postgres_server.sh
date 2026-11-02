#!/usr/bin/env bash
# Install and configure PostgreSQL for tg-ytdlp-bot (DB_ENGINE = "postgres").
#
# * TLS for every remote connection (own CA, server cert with the given names),
#   TLS >= 1.2, SCRAM-SHA-256 passwords; remote clients match only hostssl lines;
# * optional mutual TLS (client certificates) with --client-cert;
# * local bots on this VM connect over 127.0.0.1;
# * idempotent: re-running keeps the password and certificates unless asked.
#
# Usage (as root, Debian/Ubuntu):
#   scripts/db/setup_postgres_server.sh --name db.example.com [--name 203.0.113.10] \
#       [--allow 198.51.100.7/32 ...] [--client-cert] [--bot-dir /root/Telegram/tg-ytdlp-bot]
#
#   --name NAME      DNS name or IP the bots use to reach this server (cert SAN), repeatable
#   --allow CIDR     remote network allowed to connect (TLS only), repeatable;
#                    without --allow the server listens on localhost only
#   --client-cert    also require a client certificate signed by the CA (mutual TLS)
#   --issue-client N issue an extra client certificate for bot N (copy to that VM)
#   --db NAME / --user NAME   database and role (default tgytdlp / tgytdlp)
#   --bot-dir DIR    copy ca.crt (and client cert) to DIR/CONFIG/db for a bot on this VM
#   --rotate-password  generate a new password for the role
set -euo pipefail

DB=tgytdlp
DBUSER=tgytdlp
NAMES=()
ALLOW=()
CLIENT_CERT=0
ISSUE=()
BOT_DIR=""
ROTATE=0
TLS_DIR=/etc/postgresql/tgytdlp-tls
STATE_DIR=/root/.tgytdlp-db

while [ $# -gt 0 ]; do
    case "$1" in
        --name) NAMES+=("$2"); shift 2 ;;
        --allow) ALLOW+=("$2"); shift 2 ;;
        --client-cert) CLIENT_CERT=1; shift ;;
        --issue-client) ISSUE+=("$2"); shift 2 ;;
        --db) DB="$2"; shift 2 ;;
        --user) DBUSER="$2"; shift 2 ;;
        --bot-dir) BOT_DIR="$2"; shift 2 ;;
        --rotate-password) ROTATE=1; shift ;;
        -h|--help) sed -n '2,25p' "$0"; exit 0 ;;
        *) echo "unknown option $1" >&2; exit 2 ;;
    esac
done

[ "$(id -u)" = 0 ] || { echo "run as root" >&2; exit 1; }
[[ "$DB" =~ ^[a-z_][a-z0-9_]*$ && "$DBUSER" =~ ^[a-z_][a-z0-9_]*$ ]] || { echo "bad --db/--user name" >&2; exit 2; }
[ ${#NAMES[@]} -gt 0 ] || NAMES=("localhost")

log() { echo "[setup-postgres] $*"; }

if ! command -v psql >/dev/null 2>&1 || ! ls /etc/postgresql/*/main/postgresql.conf >/dev/null 2>&1; then
    log "installing PostgreSQL"
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql openssl
fi
PGVER=$(ls /etc/postgresql | grep -E '^[0-9]+$' | sort -n | tail -1)
CONF_DIR=/etc/postgresql/$PGVER/main
HBA=$CONF_DIR/pg_hba.conf
log "PostgreSQL $PGVER ($CONF_DIR)"
systemctl enable postgresql >/dev/null 2>&1 || true
pg_ctlcluster "$PGVER" main start 2>/dev/null || true

# ------------------------------------------------------------------ TLS material
install -d -m 700 -o postgres -g postgres "$TLS_DIR"
install -d -m 700 "$STATE_DIR"
if [ ! -f "$TLS_DIR/ca.key" ]; then
    log "creating CA"
    openssl req -x509 -new -nodes -newkey rsa:4096 -sha256 -days 3650 \
        -subj "/CN=tg-ytdlp-bot DB CA" -keyout "$TLS_DIR/ca.key" -out "$TLS_DIR/ca.crt" 2>/dev/null
fi
SAN=""
for n in "${NAMES[@]}"; do
    if [[ "$n" =~ ^[0-9.]+$ || "$n" == *:* ]]; then SAN+="IP:$n,"; else SAN+="DNS:$n,"; fi
done
SAN+="DNS:localhost,IP:127.0.0.1"
if [ ! -f "$TLS_DIR/server.crt" ] || [ "$(cat "$TLS_DIR/server.san" 2>/dev/null)" != "$SAN" ]; then
    log "issuing server certificate for $SAN"
    openssl req -new -nodes -newkey rsa:2048 -subj "/CN=${NAMES[0]}" \
        -keyout "$TLS_DIR/server.key" -out "$TLS_DIR/server.csr" 2>/dev/null
    printf 'subjectAltName=%s\nextendedKeyUsage=serverAuth\n' "$SAN" > "$TLS_DIR/server.ext"
    openssl x509 -req -in "$TLS_DIR/server.csr" -CA "$TLS_DIR/ca.crt" -CAkey "$TLS_DIR/ca.key" \
        -CAcreateserial -days 825 -sha256 -extfile "$TLS_DIR/server.ext" -out "$TLS_DIR/server.crt" 2>/dev/null
    echo "$SAN" > "$TLS_DIR/server.san"
fi

issue_client() {  # $1 = file name prefix; CN must equal the DB role for clientcert=verify-full
    local name="$1"
    [ -f "$TLS_DIR/client-$name.crt" ] && return
    log "issuing client certificate '$name' (CN=$DBUSER)"
    openssl req -new -nodes -newkey rsa:2048 -subj "/CN=$DBUSER" \
        -keyout "$TLS_DIR/client-$name.key" -out "$TLS_DIR/client-$name.csr" 2>/dev/null
    printf 'extendedKeyUsage=clientAuth\n' > "$TLS_DIR/client.ext"
    openssl x509 -req -in "$TLS_DIR/client-$name.csr" -CA "$TLS_DIR/ca.crt" -CAkey "$TLS_DIR/ca.key" \
        -CAcreateserial -days 825 -sha256 -extfile "$TLS_DIR/client.ext" -out "$TLS_DIR/client-$name.crt" 2>/dev/null
}
[ "$CLIENT_CERT" = 1 ] && issue_client local
for n in "${ISSUE[@]}"; do issue_client "$n"; done
chown -R postgres:postgres "$TLS_DIR"
chmod 600 "$TLS_DIR"/*.key

# ------------------------------------------------------------------ server settings
LISTEN="localhost"
[ ${#ALLOW[@]} -gt 0 ] && LISTEN="*"
psql_admin() { su postgres -c "psql -v ON_ERROR_STOP=1 -qAt $*"; }
log "configuring ssl, scram, listen_addresses=$LISTEN"
su postgres -c "psql -v ON_ERROR_STOP=1 -q" <<SQL
ALTER SYSTEM SET ssl = 'on';
ALTER SYSTEM SET ssl_cert_file = '$TLS_DIR/server.crt';
ALTER SYSTEM SET ssl_key_file = '$TLS_DIR/server.key';
ALTER SYSTEM SET ssl_ca_file = '$TLS_DIR/ca.crt';
ALTER SYSTEM SET ssl_min_protocol_version = 'TLSv1.2';
ALTER SYSTEM SET password_encryption = 'scram-sha-256';
ALTER SYSTEM SET listen_addresses = '$LISTEN';
ALTER SYSTEM SET max_connections = '200';
ALTER SYSTEM SET shared_buffers = '1GB';
ALTER SYSTEM SET effective_cache_size = '4GB';
ALTER SYSTEM SET work_mem = '16MB';
ALTER SYSTEM SET maintenance_work_mem = '256MB';
ALTER SYSTEM SET wal_compression = 'on';
ALTER SYSTEM SET idle_in_transaction_session_timeout = '60s';
ALTER SYSTEM SET log_connections = 'on';
ALTER SYSTEM SET log_min_duration_statement = '1000';
SQL

# ------------------------------------------------------------------ role + database
PASS_FILE=$STATE_DIR/$DBUSER.password
if [ ! -s "$PASS_FILE" ] || [ "$ROTATE" = 1 ]; then
    umask 077
    openssl rand -base64 48 | tr -dc 'A-Za-z0-9' | head -c 40 > "$PASS_FILE"
fi
PASS=$(cat "$PASS_FILE")
if [ "$(psql_admin "-c \"SELECT 1 FROM pg_roles WHERE rolname='$DBUSER'\"")" != "1" ]; then
    psql_admin "-c \"CREATE ROLE $DBUSER LOGIN\""
fi
# password via stdin, not the command line (ps)
su postgres -c "psql -v ON_ERROR_STOP=1 -q" <<SQL
ALTER ROLE $DBUSER WITH LOGIN PASSWORD '$PASS' CONNECTION LIMIT 150;
SQL
if [ "$(psql_admin "-c \"SELECT 1 FROM pg_database WHERE datname='$DB'\"")" != "1" ]; then
    psql_admin "-c \"CREATE DATABASE $DB OWNER $DBUSER ENCODING 'UTF8' TEMPLATE template0\""
fi
psql_admin "-c \"REVOKE ALL ON DATABASE $DB FROM PUBLIC\""

# ------------------------------------------------------------------ pg_hba
BEGIN="# >>> tg-ytdlp-bot (managed by setup_postgres_server.sh)"
END="# <<< tg-ytdlp-bot"
AUTH="scram-sha-256"
[ "$CLIENT_CERT" = 1 ] && AUTH="scram-sha-256 clientcert=verify-full"
{
    echo "$BEGIN"
    echo "host    $DB  $DBUSER  127.0.0.1/32  scram-sha-256"
    echo "host    $DB  $DBUSER  ::1/128       scram-sha-256"
    for cidr in "${ALLOW[@]}"; do
        echo "hostssl $DB  $DBUSER  $cidr  $AUTH"
    done
    echo "$END"
} > "$STATE_DIR/hba.block"
cp -a "$HBA" "$HBA.bak.$(date +%Y%m%d%H%M%S)"
# drop the old managed block, put the new one first (first match wins)
awk -v b="$BEGIN" -v e="$END" '$0==b{skip=1} !skip{print} $0==e{skip=0}' "$HBA" > "$STATE_DIR/hba.rest"
# remote clients only match the hostssl lines above (a plaintext remote login
# finds no matching line and is refused); "local" socket lines stay first
{ grep -E '^local' "$STATE_DIR/hba.rest" || true; cat "$STATE_DIR/hba.block"; grep -vE '^local' "$STATE_DIR/hba.rest" || true; } > "$HBA"
chown postgres:postgres "$HBA"
chmod 640 "$HBA"

pg_ctlcluster "$PGVER" main restart
sleep 2
psql_admin "-c 'SHOW ssl'" | grep -q on || { echo "ssl is not on" >&2; exit 1; }

# ------------------------------------------------------------------ copy CA for a local bot
if [ -n "$BOT_DIR" ]; then
    install -d -m 700 "$BOT_DIR/CONFIG/db"
    install -m 644 "$TLS_DIR/ca.crt" "$BOT_DIR/CONFIG/db/ca.crt"
    if [ "$CLIENT_CERT" = 1 ]; then
        install -m 644 "$TLS_DIR/client-local.crt" "$BOT_DIR/CONFIG/db/client.crt"
        install -m 600 "$TLS_DIR/client-local.key" "$BOT_DIR/CONFIG/db/client.key"
    fi
    log "copied certificates to $BOT_DIR/CONFIG/db"
fi

cat <<EOF

PostgreSQL is ready. Settings for CONFIG/config.py of a bot:

  USE_FIREBASE = False
  DB_ENGINE = "postgres"
  POSTGRES_HOST = "${NAMES[0]}"        # 127.0.0.1 for a bot on this VM
  POSTGRES_PORT = 5432
  POSTGRES_DB = "$DB"
  POSTGRES_USER = "$DBUSER"
  POSTGRES_PASSWORD = "<stored in $PASS_FILE>"
  POSTGRES_SSLMODE = "verify-full"     # remote bots; a bot on this VM may use 127.0.0.1 + verify-full too
  POSTGRES_SSLROOTCERT = "CONFIG/db/ca.crt"   # copy $TLS_DIR/ca.crt there
EOF
if [ "$CLIENT_CERT" = 1 ] || [ ${#ISSUE[@]} -gt 0 ]; then
cat <<EOF
  POSTGRES_SSLCERT = "CONFIG/db/client.crt"   # $TLS_DIR/client-<name>.crt
  POSTGRES_SSLKEY = "CONFIG/db/client.key"    # $TLS_DIR/client-<name>.key (chmod 600)
EOF
fi
cat <<EOF

Remote access: allowed from ${ALLOW[*]:-nowhere (localhost only)}.
Also open TCP 5432 only for those addresses in the VM firewall and in the
cloud security list (Oracle Cloud: VCN > Security List / NSG ingress rule).
Password: cat $PASS_FILE   (never commit it; config.py is gitignored)
EOF
