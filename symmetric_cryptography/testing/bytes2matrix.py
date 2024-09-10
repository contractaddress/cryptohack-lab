'''
just testing and making the functions cleaner and easier to read
'''

import s_boxes as sbx

s_box = sbx.s_box
inv_s_box = sbx.inv_s_box


message = 'python23lkajoipq'



def bytes2matrix(text):#turning the 16 bytes string into a matrix
    matrix = [list(text[i:i+4]) for i in range(0, len(text), 4)]

    return [[ord(i) for i in rows]
        for rows in matrix] #turning the matrix into decimals



state = bytes2matrix(message)


def sub_bytes(s, sbox=s_box):
    #substitues the bytes using the s_table
    return [[sbox[num] for num in row]
        for row in s]


def matrix2bytes(mtrx): #turn the matrix back into bytes
  return ''.join(chr(item) for row in mtrx for item in row)

print(sub_bytes(state, s_box)) #print 
modified_state = sub_bytes(state, s_box)

print(matrix2bytes(modified_state)) #prints modified state in ascii
