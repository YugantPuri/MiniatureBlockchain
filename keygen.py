import random
from sympy import isprime
from math import gcd

# --- Prime generation ---
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits) | 1  # make sure it's odd
        if isprime(p):
            return p

# --- Modular inverse using Extended Euclidean Algorithm ---
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# --- RSA Key Generation ---
def generate_rsa_keys(bits=16):
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
    return (e, n), (d, n)  # public, private

# --- Signing with private key ---
def sign(message, private_key):
    d, n = private_key
    return pow(message, d, n)  # signature s = m^d mod n

# --- Verifying signature with public key ---
def verify(message, signature, public_key):
    e, n = public_key
    m_prime = pow(signature, e, n)  # m' = s^e mod n
    return m_prime == message

# --- Demo ---
def main():
    print("Generating RSA keys...")
    pub, priv = generate_rsa_keys(bits=16)
    print("Public Key:", pub)
    print("Private Key:", priv)
    
    message = 42
    print("\nOriginal Message:", message)
    
    # Sign the message
    signature = sign(message, priv)
    print("Signature:", signature)
    
    # Verify the signature
    is_valid = verify(message, signature, pub)
    print("Signature valid?", is_valid)

if __name__ == "__main__":
    main()