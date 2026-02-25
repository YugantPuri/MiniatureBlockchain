import random
from sympy import isprime
from math import gcd

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits) | 1
        if isprime(p):
            return p


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def key_gen(bits=64):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# here to generate larger RSA keys, we can modify the key_gen function to generate keys of a larger bit size, such as 128 bits or 256 bits. This will allow us to use the full 160-bit hash without truncation. However, for demonstration purposes, truncating the hash to 64 bits is a simpler solution.
# for larger keys, we can simply call key_gen with bits=128 or bits=256, which will generate larger primes and thus larger RSA keys. This will allow us to use the full 160-bit hash without truncation and maintain better security.