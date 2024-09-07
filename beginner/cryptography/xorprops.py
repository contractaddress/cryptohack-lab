'''
cryptohack challenge:

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf''' 

from Crypto.Util.number import *

def key_to_decimal(key_hex):
    bytekey = bytes.fromhex(key_hex)
    decimalkey = bytes_to_long(bytekey)
    return decimalkey

key1 = key_to_decimal('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2XORkey1 = key_to_decimal('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key2 = key1^key2XORkey1
key2XORkey3 = key_to_decimal('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
key3 = key2^key2XORkey3
flagXORkey1XORkey3XORkey2 = key_to_decimal('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = key1^key3^key2^flagXORkey1XORkey3XORkey2

print(long_to_bytes(flag))
