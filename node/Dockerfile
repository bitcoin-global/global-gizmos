FROM debian:stretch-slim

# Configure users
RUN groupadd -r bitglob && useradd -r -m -g bitglob bitglob

# Add packages
RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates dirmngr gosu gpg wget \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /opt
COPY . .
COPY docker-entrypoint.sh /entrypoint.sh

# Required configs (change to override)
ARG GITHUB_TOKEN=""
ARG GITHUB_USER="fhivemind"
ARG BITCOIN_VERSION="v0.19.2"

# Install Bitcoin Global
RUN ./scripts/install-full-node.sh -v $BITCOIN_VERSION -d /bitcoin-global -t /opt
ENV PATH="/opt/bitcoin-global/src:${PATH}"

# Expose
ENV BITGLOB_DATA=/bitcoin-global
VOLUME ["/bitcoin-global"]
EXPOSE 8333 8332 8222 18333 18332 18222

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bitglobd"]