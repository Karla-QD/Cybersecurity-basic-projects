import string
import random
import hashlib

"""
    By Karla Quirós
    Reference: https://www.youtube.com/watch?v=gUod_PQgJKk
"""

def generate_password(length):
    """
    Generate a secure password with a given length.
    return: str
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def hash_password(text):
    """
    Hash a password using the MD5 algorithm.
    return: str
    """
    hash = hashlib.md5(text.encode())
    return hash.hexdigest()

if __name__ == "__main__":
    length = int(input('Enter the length of the password: '))
    password = generate_password(length)
    print(f"Generated password: {password}")

    text = input('Enter the text to hash: ')
    hashed_text = hash_password(text)
    print(f"Hashed text: {hashed_text}")
    