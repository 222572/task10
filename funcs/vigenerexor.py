def xor_encrypt(key: str, message: str) -> str:
    key_expanded =\
        (key * (len(message) // len(key) + 1))[:len(message)]
    return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key_expanded))

def xor_decrypt(key: str, ciphertext: str) -> str:
    # XOR обратим самому себе, поэтому функция идентична для шифрования и дешифрования
    return xor_encrypt(key, ciphertext)

if __name__ == '__main__':
    pass

