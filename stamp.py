import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")


import bitcoin as btc

fee = 3000

def op_return_tx(msg, priv):
	"""
	Creates a Bitcoin Tx with op_return out
	Args:
		msg  (str): the payload for op_return
		priv (str): the private key to sign the Tx

	Return:
		a string representation of hex format of transaction
		signed and ready to be sent to a Bitcoin node
	"""
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




import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Create or verify a stamp')
	parser.add_argument('-b','--balance',
						action="store_true",
	                    help='get the balance')

	parser.add_argument('-f','--file',
						action="store",
	                    help='file to be stamped or verified')

	parser.add_argument('-c','--create',
						action="store_true",
	                    help='create a new stamp for file')

	parser.add_argument('-p','--passphrase',
						action="store",
	                    help='the secret to access your private key')




	args = parser.parse_args()
	print args


	if args.balance != None:
		print get_balance()
		exit(0)





