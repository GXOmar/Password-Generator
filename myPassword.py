#! python3

# myPassword.py - Password generator and validator

# This program is a text-based experience to Generate a Random password for the user.
# and validate a password from user input.

# USAGE: py myPassword.py <command_keyword> [optional_password_length]
# see welcome_message.txt for more info on how to use it...

# A strong password should contain the following:
# 1- At least 8 characters long.
# 2- At least 1 lowercase character.
# 3- At least 1 uppercase character.
# 4- At least 1 digit.
# 5- At least 1 symbol.

import re
import sys
import colorama
import pyperclip
import generate_password

# A regex to detect string sequences.
detect_password = re.compile(r'\S+')

# A regex to check if the password is strong or not.
detect_strong_password = re.compile(r"""^
(?=.*[a-z])                          # at least 1 lowercase character
(?=.*[A-Z])                          # at least 1 uppercase character
(?=.*[0-9])                          # at least 1 digit
(?=.*[!?@#$%^&*])                    # at least 1 symbol
# (?!.*[\[\]():;,~.`'"/+=\\-_<>{}])  # make sure the password doesn't include these characters
\S{8,}$""", re.VERBOSE)


def explain(password_str: str) -> str:
    """Check what type of characters is missing from the password, return missing category(s)"""
    li = ['an uppercase', 'a lowercase', 'a digit', 'a symbol']
    for char in password_str:
        li[0] = None if char.isupper() else li[0]
        li[1] = None if char.islower() else li[1]
        li[2] = None if char.isdigit() else li[2]
        li[3] = None if char in "!?@#$%^&*" else li[3]
    
    li = [item for item in li if item != None]
    return f"{', '.join(li[:-1])} and {li[-1]}" if len(li) > 1 else f"{li[0]} character"


def unwanted_chr_in_password(password_str: str): 
    """Detect if the password has unwanted characters, return True if so"""
    for unwanted_character in password_str:
        if unwanted_character in "\[\]():;,~.`\'\"/+=\\-_<>}{":  # unwanted character string
            # when the first unwanted character occurs, the password is invalid.
            return unwanted_character  # this act like a True value.
    return False  # password check passed.


def point_on_unwanted_chr(password_str: str, unwanted_character: str) -> None:
    """Find and point the unwanted character on the password"""
    unwanted_chr_leading_position = password_str.split(unwanted_character)[0]  # return the string before the unwanted character
    two_char_filler = "--"  # compensating the 2 quote characters surrounding the user_password string in the final message.
    pointer_character = " " * len("Your password" + two_char_filler +  unwanted_chr_leading_position) + "^"  # "^" pointer character
    print(pointer_character)
    return None


def check_password(user_password: str):
    """Check if the password is strong or not, return a message about the password"""
    # detect for a password sequence
    PASSWORD_SEQUENCE = detect_password.search(user_password)
    if PASSWORD_SEQUENCE != None:

        # check for unwanted characters in PASSWORD_SEQUENCE
        unwanted_chr = unwanted_chr_in_password(user_password)
        if unwanted_chr:
            print(f"{colorama.Fore.RESET}Your password {colorama.Fore.YELLOW}\"{user_password}\"{colorama.Fore.RESET} contains unwanted characters")
            point_on_unwanted_chr(user_password, unwanted_chr)
            return False

        # check the length of PASSWORD_SEQUENCE 
        elif len(user_password) <= 7:
            print(f"{colorama.Fore.LIGHTYELLOW_EX}Your password is too short!")
            return False

        # detect and validate the password
        elif detect_strong_password.search(PASSWORD_SEQUENCE.group()) != None:  # if found it returns a strong password match
            print(f"{colorama.Fore.GREEN}Your password \"{user_password}\" is strong")
            return True

        else:          
            print(f"{colorama.Fore.RED}Your Password is NOT strong, it's missing {colorama.Fore.MAGENTA}{explain(user_password)}.")
            return False

    else: 
        print(f"{colorama.Fore.BLUE}No password detected")


def main():
    COMMAND_KEYWORDS = ("gen", "check")
    if len(sys.argv) == 1 or sys.argv[1] not in COMMAND_KEYWORDS:
        # add a welcome screen with instructions on how to use the script.
        welcome_message = open(".\welcome_message.txt", "r").read()
        print(welcome_message)

    elif len(sys.argv) >= 2:
        if sys.argv[1] == "gen":
        # generate a very strong random password with the "gen" command with a default length of 20 characters.
            try:
                # user supplied a password length!
                random_generated_password = generate_password.generate_random_password(int(sys.argv[2]))
                pyperclip.copy(random_generated_password)
                print(f"{colorama.Fore.GREEN}Password copied!")
            except (ValueError, IndexError):
                random_generated_password = generate_password.generate_random_password(20)
                pyperclip.copy(random_generated_password)
                print(f"{colorama.Fore.GREEN}Password copied!")

        elif sys.argv[1] == "check":
        # check the strength of the prompted password
            user_password = input("Enter your password: ")
            check_password(user_password)


if __name__ == "__main__":
    main()