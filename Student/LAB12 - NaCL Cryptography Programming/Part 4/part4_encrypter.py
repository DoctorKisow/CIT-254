# Part 4: ENCRYPTION: Based on the parmeters below.

### PROCESS
# Use scrypt password-hashing mechanism to produce 32-byte key from password. CPU and memory difficulty levels (iterations) were changed from the default values to SCRYPT_OPSLIMIT_INTERACTIVE and SCRYPT_MEMLIMIT_INTERACTIVE to provide a balance between difficulty and time.
# Generate a random key and protect it via symmetric key encryption (Salsa20/Poly1305 MAC) with the password-derived key. This is the "outer box".
# Take the secret payload and protect it via symmetric key encryption with the random key. This is the "inner box". This allows the password to be changed in the future without needing to re-encrypt the entire secret payload.

### This encrypted file has been saved in the following format:
# Password salt: 32 bytes
# Outer box, encrypted: 72 bytes (32 byte key + 24 byte nonce + 16 byte auth). The outer box contains the random key
# Inner box, encrypted: Variable length (variable-length payload + 24 byte nonce + 16 byte auth). The inner box contains the secret payload.

### DELIVERABLE
# The SHA-256 hash of the secret payload file. Use the pyNaCL library to compute this hash.

import argparse
import os
import getpass
import nacl.utils
from nacl.secret import SecretBox
from nacl.pwhash import scrypt

# Parameters
SALT_SIZE = 32
SCRYPT_OPSLIMIT = scrypt.OPSLIMIT_INTERACTIVE
SCRYPT_MEMLIMIT = scrypt.MEMLIMIT_INTERACTIVE

def get_password():
    """Prompt the user for a password and confirm it."""
    while True:
        password = getpass.getpass("Enter password: ")
        confirm_password = getpass.getpass("Confirm password: ")
        if password == confirm_password:
            return password.encode()
        else:
            print("Passwords do not match. Please try again.")

def encrypt_file(password, input_file, output_file):
    """Encrypt a file."""
    # Generate a random salt
    salt = os.urandom(SALT_SIZE)

    # Derive a 32-byte key from the password
    password_key = scrypt.kdf(
        SecretBox.KEY_SIZE,
        password,
        salt,
        opslimit=SCRYPT_OPSLIMIT,
        memlimit=SCRYPT_MEMLIMIT,
    )

    # Generate a random key for the inner box
    inner_key = os.urandom(SecretBox.KEY_SIZE)

    # Encrypt the payload with the inner key
    inner_box = SecretBox(inner_key)

    try:
        with open(input_file, "rb") as f:
            payload = f.read()
        inner_encrypted = inner_box.encrypt(payload)
    except FileNotFoundError:
        print("Error: Input file not found.")
        exit(1)

    # Encrypt the inner key with the password-derived key
    outer_box = SecretBox(password_key)
    outer_encrypted = outer_box.encrypt(inner_key)

    # Save the encrypted data
    with open(output_file, "wb") as f:
        f.write(salt + outer_encrypted + inner_encrypted)

    print(f"File encrypted and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt a file.")
    parser.add_argument("input", help="Path to the input file to encrypt")
    parser.add_argument("output", help="Path to the output encrypted file")
    args = parser.parse_args()

    password = get_password()
    encrypt_file(password, args.input, args.output)