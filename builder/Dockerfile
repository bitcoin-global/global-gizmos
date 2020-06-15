FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /shared


RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates sudo \
      curl gnupg-agent software-properties-common git python3 python-minimal \
      apt-cacher-ng ruby qemu-utils jq make \
      docker.io systemd

RUN git clone https://github.com/fhivemind/vmbuilder && \
    cd vmbuilder && \ 
    chmod u+x setup.py && \
    ./setup.py install && \
    cd ..

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN systemctl enable docker


# Entrypoint
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "bash" ]