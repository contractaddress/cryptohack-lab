"""
In other words, xx is a quadratic residue when it is possible to take the square root of xx modulo an integer pp.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

p=29 ints=[5,14,6,11,58,32]
"""

ints = [5,14,6,11,58, 32]
nums = [i for i in range(max(ints))]
quads = []
non_quads = []

print('\nmathematical proofs\n')


def quad_res_finder(integer):
  is_quad = False
  for number in nums:
    result = (number**2) % 29
    if result == integer and number <= 29:
     print(f"({number}**2)%29 = {result} is a quadratic residu: {number}^2 ≡ {integer} mod 29")
     is_quad = True
  
  if is_quad:
    quads.append(integer)
  else:
    non_quads.append(integer)
  


for integer in ints:
  quad_res_finder(integer)


print(f'\nquadratic residues: {quads}')
print(f'quadratic none-residues: {non_quads}')
