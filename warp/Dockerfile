FROM debian:12-slim
ARG TARGETARCH
ENV DEBIAN_FRONTEND=noninteractive

# Base deps
RUN apt-get update && apt-get install -y \
    wireguard iproute2 iptables curl ca-certificates openresolv dumb-init procps \
    && rm -rf /var/lib/apt/lists/*

# Install wgcf (multi-arch)
RUN case "$TARGETARCH" in \
        amd64)  WGCF_ARCH=linux_amd64 ;; \
        arm64)  WGCF_ARCH=linux_arm64 ;; \
        *) echo "Unsupported arch: $TARGETARCH" && exit 1 ;; \
    esac && \
    curl -L https://github.com/ViRb3/wgcf/releases/download/v2.2.29/wgcf_2.2.29_${WGCF_ARCH} \
      -o /usr/local/bin/wgcf && \
    chmod +x /usr/local/bin/wgcf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/entrypoint.sh"]
