# Python program for the extended Euclidean algorithm

def extended_gcd(a, b):
    # Base case: if a is 0, return b as GCD and coefficients 0 and 1
    if a == 0:
        return b, 0, 1
    else:
        # Recursive call: apply the algorithm to (b % a) and a
        gcd, x, y = extended_gcd(b % a, a) 
        
        return gcd, y - (b // a) * x, x 
        # '//' is floor division: rounds down to nearest integer
        # Calculate new coefficients
        # x_new = y - (b // a) * x
        # y_new = x

# Get input from user
first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))

# Apply the extended Euclidean algorithm
gcd, x, y = extended_gcd(first, second)

# Print results
print('The GCD is', gcd)
print(f'Bezout coefficients: x = {x}, y = {y}')
print(f'Verification: {first} * {x} + {second} * {y} = {gcd}')
