

#simple Euclidean algorithm to find the greatest common dividor between two numbers


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

first = int(input('number A: '))
second = int(input('number B: '))

results = gcd(first, second)
print(f'Greatest common divisor: {results}')
