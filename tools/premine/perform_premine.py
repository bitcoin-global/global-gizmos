#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
curr_path = os.path.dirname(os.path.abspath(__file__))

# Load configuration
RPC_USERNAME = os.getenv("RPC_USERNAME", "admin")
RPC_PASSWORD = os.getenv("RPC_PASSWORD", "")

# Initialize data
testnet_keys = []
mainnet_keys = []

with open(curr_path + "/testnet") as f:
    testnet_keys = f.read().splitlines()
with open(curr_path + "/mainnet") as f:
    mainnet_keys = f.read().splitlines()

# Define mining function
# Requires cpu miner with exit code (after successfully mining of a block)
def mine(net, keys):
    block = 0
    for key in keys:
        print("Mining for block #%d (%s)" % (block, key))
        command = [
            'minerd', '-a', 'sha256d', 
            '--url', 'http://127.0.0.1:18444',
            '--userpass', '%s:%s' % (RPC_USERNAME, RPC_PASSWORD),
            '--coinbase-sig', '"/bitcoin-global.io premine block #%d"' % block,
            '--coinbase-addr', key]
        print(" ".join(command))
        subprocess.check_call(command)
        block += 1

# Run for chains
if __name__ == "__main__":
    mine("testnet", testnet_keys[0:])
