FROM debian:stretch-slim

# Add data
WORKDIR /installation
COPY . .

# Required configs (change to override)
ARG GITHUB_TOKEN
ARG GITHUB_USER="fhivemind"
ARG BITCOIN_VERSION="v0.19.2"

# Install Bitcoin Global
RUN ./scripts/install-full-node.sh -v $BITCOIN_VERSION -d /bitcoin-global -t /installation

# Expose and navigate
WORKDIR /bitcoin-global
EXPOSE 8333 8332 8222 18332 18222 18333

# Runnable
CMD ["bitglobd"]
