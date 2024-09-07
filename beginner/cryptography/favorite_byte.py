'''
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d 
'''


string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytelist = [ord for ord in bytes.fromhex(string)]


for num in range(0, 127):
    xoredbytes = [num^byte for byte in bytelist]
    print(''.join(chr(xbyte) for xbyte in xoredbytes))
