FROM ubuntu:bionic
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /shared

RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates \
      curl gnupg-agent software-properties-common git python3 \
      apache2 apt-cacher-ng python-vm-builder ruby qemu-utils jq

RUN git clone https://github.com/fhivemind/vmbuilder && cd vmbuilder
RUN chmod u+x setup.py
RUN ./setup.py install && cd ..
