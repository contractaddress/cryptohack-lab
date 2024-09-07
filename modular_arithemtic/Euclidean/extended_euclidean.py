# Python program for the extended Euclidean algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 

first = int(input('enter your first number: '))
second = int(input('enter your second number: '))


gcd, x, y = extended_gcd(first, second)
print('The GCD is', gcd)
print(f'x = {x}, y = {y}')
