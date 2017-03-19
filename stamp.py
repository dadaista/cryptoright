import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")


import bitcoin as btc

fee = 3000

def op_return_tx(msg, priv):
	pub  = btc.privtopub(priv)
	addr = btc.pubtoaddr(pub,111)#111 optional, generates for testnet
	#print 'addr', addr
	h  =btc.blockr_unspent(addr)
	#print 'history',h

	balance = sum([i['value'] for i in h])
	#print 'balance', balance


	#build a get change back out
	outs = [{'value': balance - fee,
			 'address': addr}
			 ]#back to faucet


	#create a transaction
	tx_hex =btc.mktx(h,outs)



	#create a op_return hexcode
	op_ret =btc.mk_opreturn(msg)


	#generate the tx dict to append the op_ret script
	tx=btc.deserialize(tx_hex)

	tx['outs'].append({'value':0,
					'script':op_ret})

	#serialize the tx
	tx_hex = btc.serialize(tx)

	tx_hex_signed=btc.sign(tx_hex,0,priv)

	return tx_hex_signed


