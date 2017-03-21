import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")


import bitcoin as btc

fee = 3000
keyfile = "private_key.txt"

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




def ld_current_priv():
    with open(keyfile, 'r') as f:
        key = f.read()
    return key


def generate_key(secret,testnet=111):
    import os.path
    if os.path.isfile(keyfile):
        print "ERR: another key under use. Dismiss before generate anew"
        print "exiting, no operation"
        exit(-1)

    priv = btc.sha256(secret)
    pub  = btc.privtopub(priv)
    addr = btc.pubtoaddr(pub,111 if testnet else None)#111 optional, generates for testnet
    print 'new wallet address is', addr
    print 'we are using', "testnet" if testnet else "mainnet"


    

    with open(keyfile, 'w') as f:
        f.write(priv)

    print 'key is saved in', keyfile


def get_balance(addr):
    #check if you have any token left
    h  =btc.blockr_unspent(addr)
    balance = sum([i['value'] for i in h])
    return balance



    
    


import argparse

if __name__ == "__main__":
    print """ 
CryptoRight, a tool to create a blockchain stamp.
created by Davide Carboni (C)
v0.1 - March 2017

    """
    parser = argparse.ArgumentParser(description='Create or verify a stamp')
    parser.add_argument('-b',
                        action="store_true",
                        help='get the balance')

    parser.add_argument('-f',
                        action="store",
                        metavar="filename",
                        help='file to be stamped or verified')

    parser.add_argument('-g',
                        action="store",
                        metavar="secret",
                        help='generate a new key and address from secret')

    parser.add_argument('-d',
                        action="store",
                        metavar="addr",
                        help='dismiss this key and sends all funds to addr')




    args = parser.parse_args()
    print args


    if args.g:
        generate_key(args.g)
        exit(0)



    priv = ld_current_priv()
    pub  = btc.privtopub(priv) if priv else None
    addr = btc.pubtoaddr(pub,111) if pub else None

    if priv == None:
        print "No private key found. Generate one with -g secret"
        exit(-1)

    if args.b:
        print 'balance for',addr,"=",get_balance(addr)
        exit(0)


    print "exiting, no operation"
    exit(0)

