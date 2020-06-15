FROM ubuntu:bionic
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /shared

RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates sudo \
      curl gnupg-agent software-properties-common git python3 \
      apache2 apt-cacher-ng python-vm-builder ruby qemu-utils jq \
      debootstrap lxc python-cheetah parted kpartx bridge-utils make\
      ubuntu-archive-keyring firewalld

RUN git clone https://github.com/fhivemind/vmbuilder && \
    cd vmbuilder && \ 
    chmod u+x setup.py && \
    ./setup.py install && \
    cd ..

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN echo "%sudo ALL=NOPASSWD: /usr/bin/lxc-start" > /etc/sudoers.d/docker
RUN echo "%sudo ALL=NOPASSWD: /usr/bin/lxc-execute" >> /etc/sudoers.d/docker
RUN echo '#!/bin/sh -e' > /etc/rc.local
RUN echo 'brctl addbr br0' >> /etc/rc.local
RUN echo 'ip addr add 10.0.3.1/24 broadcast 10.0.3.255 dev br0' >> /etc/rc.local
RUN echo 'ip link set br0 up' >> /etc/rc.local
RUN echo 'firewall-cmd --zone=trusted --add-interface=br0' >> /etc/rc.local
RUN echo 'exit 0' >> /etc/rc.local
RUN chmod +x /etc/rc.local

ENV USE_LXC 1
ENV GITIAN_HOST_IP 10.0.3.1
ENV LXC_GUEST_IP 10.0.3.5

USER docker
