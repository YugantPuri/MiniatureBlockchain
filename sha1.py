import math

def ascii_to_binary(text):
    binary_output = ""
    for i in range(len(text)):
        char = text[i]
        binary_char = format(ord(char), '08b')
        binary_output += binary_char
    return binary_output

def preprocess(input_string):
    binary_output = ascii_to_binary(input_string)
    message_length = len(binary_output)

    # Append '1' bit
    binary_output += '1'

    # Pad with zeros until length ≡ 448 mod 512
    while (len(binary_output) % 512) != 448:
        binary_output += '0'

    # Append 64-bit big-endian message length
    length_bits = format(message_length, '064b')
    binary_output += length_bits

    # Split into 512-bit blocks
    block_array = []
    for i in range(0, len(binary_output), 512):
        block_array.append(binary_output[i:i+512])

    return block_array


def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def block_processor(blocks):
    processed_blocks = []

    for block in blocks:
        words = []
        for i in range(0, 512, 32):
            word_string = block[i:i+32]
            word_int = int(word_string, 2)
            words.append(word_int)
        processed_blocks.append(words)

    return processed_blocks

def word_gen(block):
    loop_words = block[:]
    for i in range(16, 80):
        res = loop_words[i - 3] ^ loop_words[i - 8] ^ loop_words[i - 14] ^ loop_words[i - 16]
        res = left_rotate(res, 1)
        loop_words.append(res)
    return loop_words

def sha1_gen(str):
    blocks = preprocess(str)

    H0 = 0x67452301
    H1 = 0xEFCDAB89
    H2 = 0x98BADCFE
    H3 = 0x10325476
    H4 = 0xC3D2E1F0

    processed_blocks = block_processor(blocks)

    for block in processed_blocks:
        loop_words = word_gen(block)

        a = H0
        b = H1
        c = H2
        d = H3
        e = H4

        for i in range(80):
            if i <= 19:
                f = ((b & c) | ((~b & 0xFFFFFFFF) & d)) & 0xFFFFFFFF
                k = 0x5A827999
            elif i <= 39:
                f = (b ^ c ^ d) & 0xFFFFFFFF
                k = 0x6ED9EBA1
            elif i <= 59:
                f = ((b & c) | (b & d) | (c & d)) & 0xFFFFFFFF
                k = 0x8F1BBCDC
            else:
                f = (b ^ c ^ d) & 0xFFFFFFFF
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + loop_words[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        H0 = (H0 + a) & 0xFFFFFFFF
        H1 = (H1 + b) & 0xFFFFFFFF
        H2 = (H2 + c) & 0xFFFFFFFF
        H3 = (H3 + d) & 0xFFFFFFFF
        H4 = (H4 + e) & 0xFFFFFFFF

    final_hash = (
        format(H0, '08x') +
        format(H1, '08x') +
        format(H2, '08x') +
        format(H3, '08x') +
        format(H4, '08x')
    )

    return final_hash

def hash_gen(crypt):
    sha1 = sha1_gen(crypt)
    return sha1


test_string = "Hello, World!!"
print(hash_gen(test_string))