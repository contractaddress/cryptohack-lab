'''
Complete the add_round_key function,
then use the matrix2bytes function to get your next flag.
'''

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
   new_matrix = []   
   for state_row, round_row in zip(s, k):
        for state_item, round_item in zip(state_row, round_row):
            new_matrix.append(state_item^round_item)
   return [new_matrix[i:i+4]for i in range(0,len(new_matrix),4)]

def matrix2bytes(mtrx):
  return ''.join(chr(item) for row in mtrx for item in row)

xord_matrix = add_round_key(state, round_key)
print(matrix2bytes(xord_matrix))
