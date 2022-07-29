
# generate_password.py - generate a strong random password.
# this module uses the secrets module to generate a password instead of the random module. 

import secrets
import random
import string

# sequence of characters to generate a random password
LOWERCASE_CHARACTERS = string.ascii_lowercase
UPPERCASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!?@#$%^&*"
ALL_CHARACTER_TYPES = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + DIGITS + SYMBOLS

# "Guaranteed" at least one random character from each string category when generating a random password.
# this eliminates the randomness of NOT having at least one of each character.
guarantee_one_of_each_chr_type = secrets.choice(LOWERCASE_CHARACTERS) + secrets.choice(UPPERCASE_CHARACTERS)\
     + secrets.choice(DIGITS) + secrets.choice(SYMBOLS)  # equals to 4 characters


def generate_random_password(password_length: int) -> str:
    """Generate a random password"""
    if password_length < 8:  # the length of the password should not be < 8 characters
        password_length = 8
    # Generate a random password with the length based on password_length minus the guaranteed random characters.
    # example: 12 - 4(guarantee_one_of_each_chr_type) = 8 so will generate 8 random characters.
    random_password = [secrets.choice(ALL_CHARACTER_TYPES) for _ in range(0, password_length - len(guarantee_one_of_each_chr_type))]  
    # the random_password is a list so i can shuffle the order of the characters later.
    # after generating the password we then add the missing 4 characters to the random password
    random_password.extend(guarantee_one_of_each_chr_type)
    random.shuffle(random_password)  # shuffle the list so the added 4 characters don't stay in their original order.
    return ''.join(random_password)