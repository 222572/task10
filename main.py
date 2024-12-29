from funcs.caesar import *
from funcs.vigenere import *
from funcs.vigenerexor import *
from funcs.cbc import *

# Шифр Цезаря
key = 5
message = "Hello, World!"
ciphertext = caesar_encrypt(key, message)
print("Caesar Encrypted:", ciphertext)
print("Caesar Decrypted:", caesar_decrypt(key, ciphertext))
print("Caesar Cracked:", caesar_crack(ciphertext))

# Шифр Виженера
key = "key"
ciphertext = vigenere_encrypt(key, message)
print("Vigenere Encrypted:", ciphertext)
print("Vigenere Decrypted:", vigenere_decrypt(key, ciphertext))

# Шифр Виженера с XOR
ciphertext = xor_encrypt(key, message)
print("XOR Encrypted:", ciphertext)
print("XOR Decrypted:", xor_decrypt(key, ciphertext))

# Цепочка блоков
key = "blockkey"
ciphertext = cbc_encrypt(key, message)
print("CBC Encrypted:", ciphertext)
print("CBC Decrypted:", cbc_decrypt(key, ciphertext))
