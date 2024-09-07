p = 29
ints = [5,14,6,11,58, 32]


for intgr in ints:
    resulz = pow(intgr, (p - 1)//2, p)
    if resulz == 1:
     print(intgr)


# testing legendre with ints and p
