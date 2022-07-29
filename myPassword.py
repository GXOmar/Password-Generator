#! python3

# myPassword.py - Password generator and validator

# This program is a text-based experience to Generate a Random password for the user.
# and validate a password from user input.

# USAGE: py myPassword.py <command_keyword> [optional_password_length]
# see welcome_message.txt for more info on how to use it...

from scripts_folder import generate_password
from scripts_folder import check_password
import sys
import colorama
import pyperclip


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
            check_password.check_password(user_password)


if __name__ == "__main__":
    main()