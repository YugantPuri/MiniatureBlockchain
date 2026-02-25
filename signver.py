from keygen import key_gen
from sha1 import hash_gen

public_key, private_key = key_gen(bits=128) #change it to 128 or 256 for larger keys and better security

# def sign_sha1_string(message, private_key):
#     d, n = private_key
#     message_hash = hash_gen(message)
#     truncated_hash = message_hash[:16]  # take the first 16 characters (64 bits)
#     hash_int = int(truncated_hash, 16)
#     signature = pow(hash_int, d, n)
#     return signature

# def verify_sha1_signature(message, signature, public_key):
#     e, n = public_key
#     message_hash = hash_gen(message)
#     truncated_hash = message_hash[:16]  # take the first 16 characters (64 bits)
#     hash_int = int(truncated_hash, 16)
#     hash_from_signature = pow(signature, e, n)
#     return hash_int == hash_from_signature

# # for full hash without truncation, we would need to use larger RSA keys (128 bits or 256 bits) to accommodate the full 160-bit hash. This way, we can maintain better security and avoid the risks associated with truncating the hash.
# # the functions for the larger keys are:

def sign_sha1_string_full(message, private_key):
    d, n = private_key
    message_hash = hash_gen(message)
    hash_int = int(message_hash, 16)
    signature = pow(hash_int, d, n)
    return signature

def verify_sha1_signature_full(message, signature, public_key):
    e, n = public_key
    message_hash = hash_gen(message)
    hash_int = int(message_hash, 16)
    hash_from_signature = pow(signature, e, n)
    return hash_int == hash_from_signature




# message = "Hello, World!!"
# signature = sign_sha1_string_full(message, private_key)
# print(f"Message: {message}")
# print(f"Signature: {signature}")
# is_valid = verify_sha1_signature_full(message, signature, public_key)
# print(f"Signature valid: {is_valid}")
# # printing the keys for demonstration purposes
# print(f"Public Key: {public_key}")
# print(f"Private Key: {private_key}")

# lets take the full hash and not truncate it, make the remaining code work with the full hash instead of truncating it to 16 characters (64 bits)

# its showing false because the hash is 160 bits and our RSA keys are only 64 bits, so we need to either truncate the hash to 64 bits or use larger RSA keys. For simplicity, we can truncate the hash to 64 bits by taking the first 16 characters of the hash string, which corresponds to 64 bits.
# to generate larger RSA keys, we can modify the key_gen function to generate keys of a larger bit size, such as 128 bits or 256 bits. This will allow us to use the full 160-bit hash without truncation. However, for demonstration purposes, truncating the hash to 64 bits is a simpler solution.
# or we can modify the signing and verification functions to work with the full 160-bit hash by using a larger key size for RSA, such as 128 bits or 256 bits. This way, we can use the full hash without truncation and still maintain security.
# this way security is compromised because we are only using the first 64 bits of the hash, which can lead to collisions and make it easier for attackers to forge signatures. Using larger RSA keys and the full hash is recommended for better security.

















