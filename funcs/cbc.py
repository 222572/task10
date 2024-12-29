import os

def cbc_encrypt(key: str, message: str) -> str:
    iv = ''.join(chr(b) for b in os.urandom(len(key)))  # Convert bytes to a string
    ciphertext = iv
    prev_block = iv
    key_expanded = (key * (len(message) // len(key) + 1))[:len(message)]

    for i in range(0, len(message), len(key)):
        block = message[i:i+len(key)]
        block_encrypted = ''.join(
            chr(ord(m) ^ ord(k) ^ ord(prev_block[j])) for j, (m, k) in enumerate(zip(block, key_expanded))
        )
        ciphertext += block_encrypted
        prev_block = block_encrypted

    return ciphertext


def cbc_decrypt(key: str, ciphertext: str) -> str:
    iv = ciphertext[:len(key)]
    ciphertext = ciphertext[len(key):]
    prev_block = iv
    plaintext = ''
    key_expanded = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]

    for i in range(0, len(ciphertext), len(key)):
        block = ciphertext[i:i+len(key)]
        block_decrypted = ''.join(
            chr(ord(c) ^ ord(k) ^ ord(prev_block[j])) for j, (c, k) in enumerate(zip(block, key_expanded))
        )
        plaintext += block_decrypted
        prev_block = block

    return plaintext

if __name__ == '__main__':
    pass
