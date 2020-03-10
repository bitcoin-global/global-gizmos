#!/bin/bash

# Install blockchain
# ------------------
cd ~/bitcoin
./bitcoind -daemon

# Check blocks
# ------------
./bitcoin-cli getblockcount