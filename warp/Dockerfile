FROM debian:12-slim
ARG TARGETARCH
ENV DEBIAN_FRONTEND=noninteractive

# Install all dependencies and wgcf in one layer to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    wireguard \
    iproute2 \
    iptables \
    curl \
    ca-certificates \
    openresolv \
    dumb-init \
    procps \
    dnsutils \
    && \
    # Install wgcf (multi-arch)
    case "$TARGETARCH" in \
        amd64)  WGCF_ARCH=linux_amd64 ;; \
        arm64)  WGCF_ARCH=linux_arm64 ;; \
        *) echo "Unsupported arch: $TARGETARCH" && exit 1 ;; \
    esac && \
    curl -fsSL https://github.com/ViRb3/wgcf/releases/download/v2.2.29/wgcf_2.2.29_${WGCF_ARCH} \
      -o /usr/local/bin/wgcf && \
    chmod +x /usr/local/bin/wgcf && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/* \
           /root/.cache

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/entrypoint.sh"]
