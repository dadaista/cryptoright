"""
Author Davide Carboni (Mar 2017)

This code is a simple proof of concept to create a OP_RETURN Bitcoin transaction
with a small messagge embedded. It uses testnet and faucets.

"""


import bitcoin as b

priv = b.sha256("davide")
pub  = b.privtopub(priv)
addr = b.pubtoaddr(pub,111)#111 optional, generates for testnet
print addr


#check if you have any token left
h  =b.blockr_unspent(addr)
print h


#build a get change back out
outs = [{'value': 5000,#replace with actual value
		 'address': addr}
		 ]#back to faucet


#create a transaction
tx_hex =b.mktx(h,outs)



#create a op_return hexcode
op_ret =b.mk_opreturn("hello world! by 0xdada157a")


#generate the tx dict to append the op_ret script
tx=b.deserialize(tx_hex)

tx['outs'].append({'value':0,
				'script':op_ret})


print tx

#serialize the tx
tx_hex = b.serialize(tx)

print "====== tx_hex ======"
print tx_hex



tx_hex_signed=b.sign(tx_hex,0,priv)


print "====== tx signed ======"
print b.deserialize(tx_hex_signed)

print "====== tx signed hex ======"
print tx_hex_signed

print "***************************"
print "copy and paste on https://live.blockcypher.com/"

