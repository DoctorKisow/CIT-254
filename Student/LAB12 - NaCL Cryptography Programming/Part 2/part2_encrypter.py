#!/usr/bin/python3

# Part 2: ENCRYPTER: Symmetric Encryption using a Salsa20 Stream Cipher with Poly1305 Message Authentication Code

import os
import sys
from nacl.secret import SecretBox
from nacl.utils import random

def encrypt_salsa20(plaintext, key_file, ciphertext_file):
    """Encrypt an ASCII string using Salsa20 with Poly1305."""
    try:
        # Generate a cryptographically random 32-byte symmetric key
        key = random(SecretBox.KEY_SIZE)

        # Create a SecretBox with the key
        box = SecretBox(key)

        # Encode plaintext to bytes and encrypt it
        plaintext_bytes = plaintext.encode('ascii')
        ciphertext = box.encrypt(plaintext_bytes)

        # Write the key to the key file
        with open(key_file, "wb") as key_out:
            key_out.write(key)

        # Write the ciphertext to the ciphertext file
        with open(ciphertext_file, "wb") as ciphertext_out:
            ciphertext_out.write(ciphertext)

        print("Encryption successful!")
        print(f"Encrypted message saved to '{ciphertext_file}'")
        print(f"Symmetric key saved to '{key_file}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 sym_encrypter.py <plaintext>")
        sys.exit(1)

    # Get the plaintext input from the command-line argument
    plaintext = sys.argv[1]

    # Define output file names
    key_file = "key.bin"
    ciphertext_file = "ciphertext.bin"

    # Encrypt the plaintext
    encrypt_salsa20(plaintext, key_file, ciphertext_file)
