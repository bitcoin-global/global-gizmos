#!/env/python
import os 
from blockchain_parser.blockchain import Blockchain

# clean files
open('~/bitcoin/snapshot.csv', 'w').close()
open('~/bitcoin/blocks.csv', 'w').close()

# Prepare data
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))
f = open('~/bitcoin/snapshot.csv','a+', encoding="utf-8")
blocks = open('~/bitcoin/blocks.csv','a+', encoding="utf-8")
f.write("tx|outputno|type|value\n")
blocks.write("height|block\n")

# Process data
try:
    for block in blockchain.get_ordered_blocks():
        blocks.write("%d|%s\n" % (block.height, block.hash))
        for tx in block.transactions:
            for no, output in enumerate(tx.outputs):
                f.write("%s|%d|%s|%s\n" % (tx.hash, no, output.type, output.value))
finally:
    f.close()
    blocks.close()
