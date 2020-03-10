#!/bin/bash
# Create required folders
mkdir ~/downloads

# Update & Upgrade the System
# ---------------------------
# sudo apt-get install -y software-properties-common
# sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get upgrade


# Install required packages
# -------------------------
sudo apt-get install -y build-essential libtool autotools-dev autoconf pkg-config libssl-dev
sudo apt-get install -y libboost-all-dev
sudo apt-get install -y libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler
sudo apt-get install -y libqrencode-dev autoconf openssl libssl-dev libevent-dev
sudo apt-get install -y libminiupnpc-dev
sudo apt-get install -y libleveldb-dev libdb4.8-dev libdb4.8++-dev

# Install Berkley DB 4.8
# ----------------------
cd ~/downloads
if [ ! -e db-4.8.30 ]
then
   wget http://download.oracle.com/berkeley-db/db-4.8.30.tar.gz
   tar zxvf db-4.8.30.tar.gz
   rm -f db-4.8.30.tar.gz
fi

cd db-4.8.30/build_unix
../dist/configure --prefix=/usr/local --enable-cxx
make
sudo make install
cd ~/downloads
rm -fr db-4.8.30/

# Download and install Bitcoin Source code
# ----------------------------------------
cd ~/downloads
if [ ! -e bitcoin ]
then
   git clone https://github.com/bitcoin/bitcoin ~/downloads/bitcoin
fi

cd bitcoin
./autogen.sh
./configure
make
sudo make install

cd ~/downloads
rm -fr bitcoin