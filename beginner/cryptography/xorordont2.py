'''
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
'''

from itertools import cycle

string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'




cipherbytes = bytes.fromhex(string)
known_flag = b'crypto{'

print(bytes(c^kf for c, kf in zip(cipherbytes, cycle(known_flag))))
#b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'

key = b'myXORkey'

print(bytes(c^k for c, k in zip(cipherbytes, cycle(key))))

