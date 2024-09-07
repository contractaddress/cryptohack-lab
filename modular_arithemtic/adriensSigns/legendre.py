'''
using legendre to see if 'a' is a quadratic residue of mod 'p'
'''

def legendre(a, p):
    if p <= 1:
        raise ValueError("p must be a prime greater than 1")
    
    if a % p == 0:
        return True  # 0 is always a quadratic residue modulo any prime
    
    # Compute the Legendre symbol (a/p)
    legendre_symbol = pow(a, (p - 1) // 2, p)
    
    if legendre_symbol == 1:
        return f'{a} is a quadratic residue modulo {p}'
    elif legendre_symbol == p - 1:
        return f'{a} is not a quadratic residue modulo {p}'
    else:
        raise ValueError("Unexpected result from Legendre symbol computation")

# Example usage:
a = 288260533169915
p = 1007621497415251
print(legendre(a, p))
