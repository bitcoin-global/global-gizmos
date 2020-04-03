# This script generates predefined amount of pub/priv keys
# using cryptographically secure secp256k1
import coincurve
import secrets
import sys

# Predefined values
# We save public and private keys to __CHAIN__ files, and public key arrays to __CHAIN_CONSTS__ file
__CHAIN__ = {
    "mainnet": {"size": 100, "file": open("secret.mainnet.csv", "w")},
    "test": {"size": 50, "file": open("secret.testnet.csv", "w")},
    "reg": {"size": 5, "file": open("secret.regtest.csv", "w")}
}
__CHAIN_CONSTS__ = open("param_consts.cpp", "w")
__OUT_FORMAT__ = """// Chain: %s
vPreminePubkeys = {
    %s
};
"""

# Minimal class definition for crypto-secure random key
class RandKey():
    def __init__(self):
        secret = secrets.token_bytes(32)
        self.private_key = coincurve.PrivateKey(secret)

    def pub(self):
        return self.private_key.public_key.format(True).hex()

    def priv(self):
        return self.private_key.to_hex()

    def __str__(self):
        return "%s|%s\n" % (self.pub(), self.priv())    

def get_keys(size):
    return [RandKey() for i in range(size)]

# Perform all operations
if __name__ == "__main__":
    for key, chain in __CHAIN__.items():
        print("%s - Performing operations" % key)
        
        # generate keys
        generated_keys = get_keys(chain["size"])

        # save pub keys to consume in client
        __CHAIN_CONSTS__.write(__OUT_FORMAT__ % (key, ", ".join(["\"%s\"" % x.pub() for x in generated_keys])))
        
        # save all keys
        chain["file"].write("public key|private key\n")
        for key in generated_keys:
            chain["file"].write(str(key))
        chain["file"].close()
    __CHAIN_CONSTS__.close()

    print("Finished")
    sys.exit(0)
