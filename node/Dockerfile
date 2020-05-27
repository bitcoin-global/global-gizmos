FROM debian:stretch-slim

# Configure users
RUN groupadd -r bitglob && useradd -r -m -g bitglob bitglob

# Add data
WORKDIR /installation
COPY . .

# Required configs (change to override)
ENV BITCOIN_FOLDER /bitcoin-global
ARG GITHUB_TOKEN
ARG GITHUB_USER="fhivemind"
ARG BITCOIN_VERSION="v0.19.2"

# Install Bitcoin Global
RUN ./scripts/install-full-node.sh -v $BITCOIN_VERSION -d $BITCOIN_FOLDER -t /installation

# Expose
VOLUME $BITCOIN_FOLDER
EXPOSE 8333 8332 8222 18332 18222 18333

WORKDIR $BITCOIN_FOLDER

# Runnable
ENTRYPOINT ["/installation/docker-entrypoint.sh"]
CMD ["bitglobd"]
