#!/usr/bin/env python3

# This file serves to update WIF to work with Electrum wallets.
# Copy this file to Electrum folder along with mainnet and testnet
# files.
# Should work fine.

from electrum import bitcoin
from electrum import ecc
from electrum import wallet
import pandas as pd

if __name__ == '__main__':
    ### Mainnet
    constants.set_mainnet()
    df = pd.read_csv("./secret.mainnet.csv", sep='|', header=0, dtype=object, encoding='ascii', engine='python')
    df = pd.DataFrame(df) 
    df['wif'] = df.apply(lambda row: bitcoin.serialize_privkey(bytes.fromhex(row.private_key), True, "p2pk").replace('p2pk:',''), axis = 1) 
    df['btg_address'] = df.apply(lambda row: bitcoin.address_from_private_key(bitcoin.serialize_privkey(bytes.fromhex(row.private_key), True, "p2pk").replace('p2pk:','')), axis = 1) 
    df.to_csv('./secret.mainnet-updated.csv', sep=',', index=False)
    
    ### Testnet
    constants.set_testnet()
    df = pd.read_csv("./secret.testnet.csv", sep='|', header=0, dtype=object, encoding='ascii', engine='python')
    df = pd.DataFrame(df) 
    df['wif'] = df.apply(lambda row: bitcoin.serialize_privkey(bytes.fromhex(row.private_key), True, "p2pk").replace('p2pk:',''), axis = 1) 
    df['btg_address'] = df.apply(lambda row: bitcoin.address_from_private_key(bitcoin.serialize_privkey(bytes.fromhex(row.private_key), True, "p2pk").replace('p2pk:','')), axis = 1) 
    df.to_csv('./secret.testnet-updated.csv', sep=',', index=False)
