def caesar_encrypt(k: int, msg: str) -> str:
    return ''.join( 
        chr(
            (ord(char) + k) % 65536
        ) for char in msg
    )

def caesar_decrypt(k: int, cypher: str) -> str:
    return ''.join(
        chr(
            (ord(ch) - k) % 65536
        ) for ch in cypher
    )

def caesar_crack(ciphertext: str) -> str:
    frequency = {char: ciphertext.count(char) for char in set(ciphertext)}
    most_common_char = max(frequency, key=frequency.get)

    assumed_space = ' '

    k = (ord(most_common_char) - ord(assumed_space)) % 65536

    return caesar_decrypt(k, ciphertext)


if __name__ == '__main__':
    pass
