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
ARG BITCOIN_PORT="8222"
ARG BITCOIN_VERSION="v0.19.2"

# Install Bitcoin Global
RUN ./scripts/install-full-node.sh -p $BITCOIN_PORT -v $BITCOIN_VERSION -t $BITCOIN_FOLDER

# Expose
VOLUME $BITCOIN_FOLDER
EXPOSE 8332 8222 18332 18222

# Runnable
CMD ["bitglobd"]
