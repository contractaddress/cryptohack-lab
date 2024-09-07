'''
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
'''

from Crypto.Util.number import *
from itertools import cycle

string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'


cipherbyteslist = [o for o in bytes.fromhex(string)]
flagbytes = [o for o in bytes(b'crypto{')]

potential_key = [cipherbyteslist[i] ^ flagbytes[i] for i in range(len(flagbytes))]
print(''.join(chr(character) for character in potential_key))
#output myXORke
#maybe myXORkey?

cipherbytes = bytes.fromhex(string)
key = b'myXORkey'

print(bytes(c^k for c, k in zip(cipherbytes, cycle(key))))

