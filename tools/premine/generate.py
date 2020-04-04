#!/usr/bin/env python3
# This script generates predefined amount of pub/priv keys
# using cryptographically secure secp256k1
import coincurve
import secrets
import sys
from util import *

class ChainKey(object):
    """ Minimal class definition for crypto-secure random key.
    Defines key generation and conversion operations.
    """
    def __init__(self, prefix, secret_bytes):
        ''' Generates a random secp256k1 key based on input secret seed '''
        secret = secrets.token_bytes(32)
        self.secret = secret
        self.prefix = prefix
        self.secret_bytes = secret_bytes
        self.private_key = coincurve.PrivateKey(secret)

    def pub(self):
        ''' Returns public key as hex string '''
        return self.private_key.public_key.format(True).hex()

    def priv(self):
        ''' Returns private key as hex string '''
        return self.private_key.to_hex()

    def wif(self):
        ''' Returns wallet input format key as hex string '''
        return privToWif(self.priv(), self.secret_bytes)

    @staticmethod
    def csv_header():
        return "btg address|public key|wif|private key"

    def __str__(self):
        return "%s|%s|%s|%s" % (btg_address(self.pub(), self.prefix), self.pub(), self.wif(), self.priv())    

class ChainGen(object):
    """ Defines key generator class for a specified chain.
    Usages: to generate, and to save keys.
    """
    def __init__(self, chain):
        ''' Creates private keys for a specified chain '''
        self.chain = chain
        self.file = consts.CHAIN[chain]["file"]
        self.size = consts.CHAIN[chain]["size"]
        self.prefix = consts.CHAIN[chain]["prefix"]
        self.bytes = consts.CHAIN[chain]["secret_bytes"]
        self.keys  = [ChainKey(self.prefix, self.bytes) for i in range(self.size)]

    def to_csv(self):
        ''' Saves generated keys to csv file '''
        print("Saving to %s..." % self.file)
        file = open(self.file, "w")
        file.write("id|%s\n" % ChainKey.csv_header())
        for id in range(len(self.keys)):
            file.write("%d|%s\n" % (id, str(self.keys[id])))
        file.close()
    
    def to_cpp(self):
        ''' Saves generated keys to cpp vector '''
        print("Updating vector file %s..." % consts.CPPFILE)
        file = open(consts.CPPFILE, "a")
        temp_keys = reshape(self.keys, 20)
        out = ""
        for i in range(len(temp_keys)):
            out += "\t" + (", ".join(["\"%s\"" % key.pub() for key in temp_keys[i]]))
            out += "\n" if i < (len(temp_keys) - 1) else ""
        file.write(consts.VECTOR_TEMPLATE % (self.chain, out))
        file.close()

# perform operations
if __name__ == "__main__":
    if input("This will overwrite everything. Are you sure? (y/n)") != "y":
        sys.exit(0)

    print("Starting...")
    chains = ["main", "test", "reg"]
    open(consts.CPPFILE, "w").close()
    for chain in chains:
        gen_chain = ChainGen(chain)
        gen_chain.to_csv()
        gen_chain.to_cpp()
    print("Finished...")
    sys.exit(0)
