# the lines below load
# bitcoin lib from egg in the path
# the egg here provided is a fork with op_return
# implemenetation

import sys
sys.path.append("./bitcoin-2.6.11-py2.7.egg")
import bitcoin as btc


def op_return_tx(msg, priv, fee=100000):
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
    print 'history',h

    balance = sum([i['value'] for i in h])
    #print 'balance', balance


    #build a get change back out
    outs = [{'value': balance - fee,
             'address': addr}
             ]


    #create a transaction
    tx_hex =btc.mktx(h,outs)



    #create a op_return hexcode
    op_ret =btc.mk_opreturn(msg)


    #generate the tx dict to append the op_ret script
    tx=btc.deserialize(tx_hex)

    tx['outs'].append({'value':0,
                       'script':op_ret})

    print "====== tx ======"
    print tx


    #serialize the tx
    tx_hex = btc.serialize(tx)
    print "====== tx_hex ======"
    print tx_hex

    tx_hex_signed=btc.sign(tx_hex,0,priv)
    print "====== tx signed ======"
    print btc.deserialize(tx_hex_signed)

    print "====== tx signed hex ======"
    print tx_hex_signed

    return tx_hex_signed

if __name__ == '__main__':
    
    priv = btc.sha256("bibibi")
    print priv
    f=open("pippo")
    msg=f.read()

    payload = btc.sha256(msg)[:32]
    op_return_tx("sha256:"+payload,priv)


