FROM ubuntu:bionic

# Define environment configuration
ENV DOCKER_CHANNEL=stable \
    DOCKER_VERSION=19.03.2 \
    DOCKER_COMPOSE_VERSION=1.24.1 \
    DOCKER_SQUASH=0.2.0 \
    DEBIAN_FRONTEND=noninteractive \
    VM_BUILDER_SHA=bbf1921aa090eb924379cca38838d7bb8009a781 \
    GITIAN_BUILDER_SHA=bd59d446512b76f37670d40e3e2d52f6a574cc23


# Install required packages
RUN apt-get update && \
    apt-get -y install \
        bash \
        curl \
        python-pip \
        python-dev \
        iptables \
        util-linux \
        ca-certificates \
        gcc \
        libc-dev \
        libffi-dev \
        libssl-dev \
        apache2 \
        # shared builder tools
        ruby git make wget curl sudo apt-cacher-ng \
        # kvm builder
        python-vm-builder qemu-kvm qemu-utils \
        # lxc builder
        lxc debootstrap \
        net-tools \
        iproute2 \
        && \
    curl -fL "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz" | tar zx && \
    mv /docker/* /bin/ && chmod +x /bin/docker* && \
    pip install docker-compose==${DOCKER_COMPOSE_VERSION} && \
    curl -fL "https://github.com/jwilder/docker-squash/releases/download/v${DOCKER_SQUASH}/docker-squash-linux-amd64-v${DOCKER_SQUASH}.tar.gz" | tar zx && \
    mv /docker-squash* /bin/ && chmod +x /bin/docker-squash* && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache && \
    # Install vmbuilder
    git clone https://github.com/fhivemind/vmbuilder && cd vmbuilder && \
    git checkout $VM_BUILDER_SHA && \
    chmod u+x ./setup.py && ./setup.py install && \
    # Empty docker service config
    echo "" > /lib/systemd/system/docker.service && \
    # Allow nonpw invocation of sudo
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Add gitian builder
WORKDIR /shared
RUN git clone https://github.com/devrandom/gitian-builder.git && \
    git -C ./gitian-builder checkout $GITIAN_BUILDER_SHA

# Make entrypoint
COPY docker-entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/bin/entrypoint.sh"]
