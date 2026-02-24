from sha1 import hash_gen

word = 'yugant'

nonce = 0

hashed = hash_gen(word)


if (hashed[0:3] == '000'):
    print(hashed)
else:
    while(True):
        nuevo = word + str(nonce)
        hashed = hash_gen(nuevo)
        if (hashed[0:3] == '000'):
            print(hashed)
            print(nonce)
            break
        else:
            nonce += 1

