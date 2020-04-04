#!/bin/bash

# Install blockchain
# ------------------
bitcoind -daemon

# Check blocks
# ------------
bitcoin-cli getblockcount