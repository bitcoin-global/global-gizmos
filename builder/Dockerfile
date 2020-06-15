FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /shared

RUN apt-get update
RUN apt-get -y install git apache2 apt-cacher-ng python-vm-builder \ 
    ruby qemu-utils qemu-kvm sudo make wget

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN git clone https://github.com/fhivemind/vmbuilder && \
    cd vmbuilder && \ 
    chmod u+x setup.py && \
    ./setup.py install && cd ..
RUN git clone git://github.com/devrandom/gitian-builder.git

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "bash" ]