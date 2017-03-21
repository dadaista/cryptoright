# Cryptoright
Some code to use blockchains as proof-of-authorship or crypto copyright

# Dependencies
This code depends on pybitcointools as forked here https://github.com/wizardofozzie/pybitcointools
You don't need to setup anything. The pybitcointools with op_return is available here in the .egg file.

See poc.py for use

# Important
This code has not releases yet. It is in progress even the master. Code can be broken. A first release is foreseen for April 2017


# Tentative Manual of use
Will change soon

```
CryptoRight, a tool to create a blockchain stamp.
created by Davide Carboni (C)
v0.1 - March 2017

usage: stamp.py [-h] [-b] [-f filename] [-g secret] [-d addr]

Create or verify a stamp

optional arguments:
  -h, --help   show this help message and exit
  -b           get the balance
  -f filename  file to be stamped or verified
  -g secret    generate a new key and address from secret
  -d addr      dismiss this key and sends all funds to addr
```

