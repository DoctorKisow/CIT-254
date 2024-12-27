#!/usr/bin/python3

# Part 1: ENCRYPTER: One-Time Pad Cryptography

import os
import sys
from nacl.utils import random

def generate_otp(length):
    """Generate a cryptographically secure one-time pad."""
    return random(length)

def encrypt_with_otp(plaintext):
    """Encrypt the plaintext using a one-time pad."""
    # Encode plaintext to bytes
    plaintext_bytes = plaintext.encode('ascii')

    # Generate a one-time pad of the same length as the plaintext
    otp = generate_otp(len(plaintext_bytes))

    # XOR each byte of the plaintext with the corresponding byte of the OTP
    ciphertext = bytes([p ^ o for p, o in zip(plaintext_bytes, otp)])

    return ciphertext, otp

def write_to_file(filename, data):
    """Write binary data to a file."""
    with open(filename, "wb") as file:
        file.write(data)

if __name__ == "__main__":
    # Get plaintext input from the user
    if len(sys.argv) != 2:
        print("Usage: python3 otp_encrypter.py <plaintext>")
        sys.exit(1)

    plaintext = sys.argv[1]

    try:
        # Encrypt the plaintext and generate OTP
        ciphertext, otp = encrypt_with_otp(plaintext)

        # Save ciphertext and OTP to files
        write_to_file("ciphertext.bin", ciphertext)
        write_to_file("otp.bin", otp)

        print("Encryption successful!")
        print("Encrypted message saved to 'ciphertext.bin'")
        print("One-time pad saved to 'otp.bin'")
    except Exception as e:
        print(f"Error: {e}")
