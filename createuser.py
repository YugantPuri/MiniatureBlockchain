
from keygen import key_gen


public_key, private_key = key_gen(bits=128)

# create users and store their both keys in a file for later use in signing and verifying messages
with open("users.txt", "w") as f:
    f.write(f"Public Key: {public_key}\n")
    f.write(f"Private Key: {private_key}\n")

# example of how to read the keys from the file
with open("users.txt", "r") as f:
    lines = f.readlines()
    public_key_line = lines[0].strip()
    private_key_line = lines[1].strip()
    print(public_key_line)
    print(private_key_line)

#example of how to use the keys for signing and verifying messages
from signver import sign_sha1_string_full, verify_sha1_signature_full
message = "Hello, World!!"
signature = sign_sha1_string_full(message, private_key)
print(f"Message: {message}")
print(f"Signature: {signature}")
is_valid = verify_sha1_signature_full(message, signature, public_key)
print(f"Signature valid: {is_valid}")

