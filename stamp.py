import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")


import bitcoin as btc
from cryptoright import *

fee = 100000
keyfile = "private_key.txt"




import os.path

def ld_current_priv():
    if not os.path.isfile(keyfile):
        print "ERR: wallet not found. Create one with -g"
        print "exiting, no operation"
        exit(-1)

    with open(keyfile, 'r') as f:
        key = f.read()
    return key

def generate_key(secret,testnet=111):
    
    if os.path.isfile(keyfile):
        print "ERR: another key under use. Dismiss before generate anew"
        print "exiting, no operation"
        exit(-1)

    priv = btc.sha256(secret)
    pub  = btc.privtopub(priv)
    addr = btc.pubtoaddr(pub,111 if testnet else None)#111 optional, generates for testnet
    print 'new wallet address is', addr
    print 'we are using', "testnet" if testnet else "mainnet"
    print 'fill this address with some coins to pay fees'


    

    with open(keyfile, 'w') as f:
        f.write(priv)

    print 'key is saved in', keyfile


def get_balance(addr):
    #check if you have any token left
    h  =btc.blockr_unspent(addr)
    balance = sum([i['value'] for i in h])
    return balance


def sign_n_send(filename,priv,addr,fee):
    if not os.path.isfile(filename):
        print "ERR: file not found"
        print "exiting, no operation"
        exit(-1)

    balance = get_balance(addr)

    if balance<fee:
        print "ERR: not enough funds, refill wallet",addr
        exit(-1)

    f = open(filename,"r")
    content = f.read()
    hashed = btc.sha256(content)
    print "hash\n"
    print hashed
    print ""


    sig_tx=op_return_tx('sha256:'+hashed,priv)

    print "transaction hex is\n"
    print sig_tx
    #raise(Exception('not finished'))
    tid = btc.blockr_pushtx(sig_tx, 'testnet')

    return tid







    
    


import argparse

if __name__ == "__main__":
    print """ 
CryptoRight, a tool to create a blockchain stamp.
created by Davide Carboni (C)
v0.1 - 2017

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

    parser.add_argument('-fee',
                        action="store",
                        metavar="fee",
                        default=fee,
                        help='the fee for each stamp, default is 3000 satoshis')



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

    if args.f:
        tid = sign_n_send(args.f,priv,addr,int(args.fee))
        print "signed on transaction",tid
        exit(0)


    print "exiting, no operation"
    exit(0)

