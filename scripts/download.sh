#!/bin/bash

# Install blockchain
# ------------------
cd ~/bitcoin
./bitcoind

# Check blocks
# ------------
./bitcoin-cli getblockcount