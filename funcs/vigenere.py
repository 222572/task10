def vigenere_encrypt(key: str, message: str) -> str:
    key_expanded =\
        (key * (len(message) // len(key) + 1))[:len(message)]
    return ''.join(chr((ord(m) + ord(k)) % 65536) for m, k in zip(message, key_expanded))

def vigenere_decrypt(key: str, ciphertext: str) -> str:
    key_expanded =\
        (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    return ''.join(chr((ord(c) - ord(k)) % 65536) for c, k in zip(ciphertext, key_expanded))

if __name__ == '__main__':
    pass
