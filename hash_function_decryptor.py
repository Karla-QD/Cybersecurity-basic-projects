import hashlib
"""
    By Karla Quirós
    Reference: https://www.youtube.com/watch?v=gUod_PQgJKk
"""

def dictionary_attack(hash_file, dic_file):
    """
    Perform a dictionary attack to find the password corresponding to a given hash.

    Parameters:
    - hash_file (str): The hash value to crack.
    - dic_file (str): Path to the dictionary file containing potential passwords.

    Returns:
    - str or None: The password if found, otherwise None.
    """
    with open(dic_file, "r") as file:
        for line in file:
            password = line.strip()  # Remove newline characters
            hash_calculated = hashlib.md5(password.encode()).hexdigest()

            if hash_calculated == hash_file:
                return password
    
    return None  # Password not found

if __name__ == "__main__":
    hash_file = hashlib.md5("test".encode()).hexdigest()
    dic_file = input("Enter the dictionary file: ")

    password_found = dictionary_attack(hash_file, dic_file)
    if password_found:
        print(f"Password found: {password_found}")
    else:
        print("Password not found in the dictionary.")
