"""
Author Davide Carboni (Mar 2017)

This code is a simple proof of concept to create a OP_RETURN Bitcoin transaction
with a small messagge embedded. It uses testnet and faucets.

"""

# the lines below load
# bitcoin lib from egg in the path
# the egg here provided is a fork with op_return
# implemenetation

#import sys
#sys.path.append("./bitcoin-2.6.11-py2.7.egg")


#%%
import bitcoin as b


priv = b.sha256("baba")
pub  = b.privtopub(priv)
addr = b.pubtoaddr(pub,111)#111 optional, generates for testnet
print 'addr', addr


#check if you have any token left
h  =b.blockr_unspent(addr)
print 'history',h

balance = sum([i['value'] for i in h])
print 'balance', balance

fee = 3000



#build a get change back out
outs = [{'value': balance - fee,'address': addr}]#


#%create a transaction
tx_hex =b.mktx(h,outs)



#create a op_return hexcode
tx_opr=b.mk_opreturn("hello world! by mepppp",tx_hex)


assert(tx_opr != tx_hex)

#%%
#generate the tx dict to append the op_ret script
#tx=b.deserialize(tx_hex)

#tx['outs'].append({'value':0,'script':op_ret})

print "====== tx_opr ======"
print tx_opr

#serialize the tx
#tx_hex = b.serialize(tx)

#print "====== tx_hex ======"
#print tx_hex



tx_hex_signed=b.sign(tx_opr,0,priv)


print "====== tx signed ======"
print b.deserialize(tx_hex_signed)

print "====== tx signed hex ======"
print tx_hex_signed

print "***************************"
print "copy and paste on https://live.blockcypher.com/"

