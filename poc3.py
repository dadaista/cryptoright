#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:28:08 2017

@author: root
"""

from web3 import Web3, KeepAliveRPCProvider, IPCProvider
w=Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

eth=w.eth