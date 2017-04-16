#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 00:26:03 2017

@author: root
"""

"""
Author Davide Carboni (Mar 2017)

This code is a simple proof of concept to create a Bitcoin transaction
It uses testnet and faucets.

"""

# the lines below load
# bitcoin lib from egg in the path
# the egg here provided is a fork with op_return
# implemenetation

import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")



import bitcoin as b


priv = b.sha256("dvdcrb")
pub  = b.privtopub(priv)
addr = b.pubtoaddr(pub,111)#111 optional, generates for testnet
print 'addr', addr


#check if you have any token left
h  =b.blockr_unspent(addr)
print 'history',h

balance = sum([i['value'] for i in h])
print 'balance', balance

fee = 400000



#%%build a get change back out
outs = [{'value': balance - fee,
		 'address': addr}
		 ]#back to faucet


#%%create a transaction
tx_hex =b.mktx(h,outs)





print "====== tx_hex ======"
print tx_hex



tx_hex_signed=b.sign(tx_hex,0,priv)


print "====== tx signed ======"
print b.deserialize(tx_hex_signed)

print "====== tx signed hex ======"
print tx_hex_signed

print "***************************"
print "copy and paste on https://live.blockcypher.com/"

