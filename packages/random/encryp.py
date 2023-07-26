import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    cipher_text += key[chars.index(letter)]

print(plain_text)
print(cipher_text)

# decrypt
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    plain_text += chars[key.index(letter)]

print(cipher_text)
print(plain_text)
