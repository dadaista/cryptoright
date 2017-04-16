#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Creates a ethereum transaction with a string attached
Requires 2 accounts available and some ether
see CREATE_PRIVATE_CHAIN.readme
@author: davide
"""
#%%
from web3 import Web3, KeepAliveRPCProvider, IPCProvider, EthereumTesterProvider
w=Web3(IPCProvider())

#w=Web3(EthereumTesterProvider())
eth=w.eth

#print accounts
#create one if empty
print eth.accounts

acc=eth.accounts[0]
print acc


print {a:eth.getBalance(a) for a in eth.accounts}

#%%

tx=  {"from":eth.accounts[0],
      "to":eth.accounts[1],
      "value":10000000000,
      'data':w.toHex('John Doe says hello!')}

w.personal.unlockAccount(acc, "davide", 1000);

eth.sendTransaction(tx)

