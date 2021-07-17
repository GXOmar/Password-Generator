
# This Program is a text based experience to Generate a Random password for the user.
# and also to ask the user to enter a password to check if it's strong or not.

# a strong password should contain the following:
# 1 >>> at least 8 characters long.
# 2 >>> at least 1 upper 
# 3 >>> at least 1 lower case letter.
# 4 >>> at least 1 digit.
# 5 >>> at least 1 symbol

import re
import string
import random
import secrets
import colorama
import pyperclip

# create a Regex to check the password first.
detectPW = re.compile(r'\S+')

# create a Regex to check if the password strong or not.
StrongPW = re.compile(r'''^
(?=.*[a-z])                          # at least one lower case letter
(?=.*[A-Z])                          # at least one upper case letter
(?=.*[0-9])                          # at least one digit
(?=.*[!?@#$%^&*])                    # at least one symbol
# (?!.*[\[\]():;,~.`'"/+=\\-_<>{}])  # make sure the PW doesn't include these characters
\S{8,}$''', re.VERBOSE)

# DONE: Generate a Random PASSWORD 
# DONE: let the user choose the length of the password
# DONE: make a choice for the user to select the level of the password (weak, medium, strong or very strong)
# DONE: copy the strong PW to the clipboard. 
# DONE: make an Explanation why the Password is not strong, e.g. Missing a Number! 
# _____________________________________________________ 
# TODO: implement a GUI for this program 
# TODO: make a strength bar to indecate the PW strength insted of "(weak, medium, strong or very strong)".
# TODO: let the user choice one or multiple character types to generate a PW around it e.g. only symbols

# sequence of characters for the random password
lower_case, upper_case = string.ascii_lowercase, string.ascii_uppercase
digit, symbols = string.digits, '!?@#$%^&*'
all = lower_case + upper_case + digit + symbols

R_lowercase, R_uppercase = secrets.choice(lower_case), secrets.choice(upper_case)
R_digit, R_symbols = secrets.choice(digit), secrets.choice(symbols) 
R_all = R_lowercase + R_uppercase + R_digit + R_symbols # eqaul to 4 character

# guaranteed Random characters
Random_character_values = {
    'weak' : R_lowercase,
    'medium' : R_lowercase + R_uppercase,
    'strong' : R_lowercase + R_uppercase + R_digit,
    'very strong' : R_all
    # 'symbols' : R_symbols
}

# ask the user for the password strength (weak, medium, strong or vere strong)
# each key(string) is an optional user input that represent PW strength(category of character), strong by default.
PWstrength_chars = {
    'weak': lower_case,
    'medium' : lower_case + upper_case,
    'strong' : lower_case + upper_case + digit, 
    'very strong' : all, 
    # 'symbols' : symbols
} 
    
def GeneratePW(length, PW_strength):
    '''this function will generate a random password and return it'''
    # length of PW should not be < 4
    if length <= 6:
        length = 8
    # First generate length-Random_sequence of characters in a list minus the length of guaranteed Random characters. 
    # e.g. 12 - 4(R_all) = 8 so will generate 8 random character.
    Random_PW = [secrets.choice(PWstrength_chars[PW_strength]) for _ in range(0, length - len(Random_character_values[PW_strength]))]
    # we add the guaranteed Random characters so we make sure the randomly genarated PW include what the user asked for.
    # e.g. add the last 4(from R_all) remaning character so we get 12 character back.
    Random_PW.extend(Random_character_values[PW_strength])
    # shuffle the list so the added Random_characters don't stay in order.
    random.shuffle(Random_PW)
    return ''.join(Random_PW)


def explain(PWstr):
    '''This Function will check what character type is missing in the password, return what's missing'''
    li = ['lowe case', 'upper case', 'digit', 'symbol']
    for char in PWstr:
        li[0] = None if char.islower() else li[0]
        li[1] = None if char.isupper() else li[1]
        li[2] = None if char.isdigit() else li[2]
        li[3] = None if char in '!?@#$%^&*' else li[3]
    
    li = [item for item in li if item != None]
    return ', '.join(li[:-1]) + ' and ' + li[-1] if len(li) > 1 else li[0]

def unwanted_ch_list(PWstr): 
    '''this function is to detect if PW has unwanted characters, return True if so'''
    matched_list = [character in '\[\]():;,~.`\'\"/+=\\-_<>}{' for character in PWstr]   
    if any(matched_list): # if one unwanted char found in PW, PW is invalid
        return True
    return False

def checkPW(user_passwrod):
    '''This function is to check the PW strong or not and return the final output'''
    # detect if Pw
    PW = detectPW.search(user_passwrod)
    if PW != None: # means it return a 'PW' match

        # search for Strong PW
        SPW = StrongPW.search(PW.group())

        # check for unwanted characters in PW
        if unwanted_ch_list(user_passwrod):
            return f"{colorama.Fore.RESET}Your password {colorama.Fore.YELLOW}\"{user_passwrod}\"{colorama.Fore.RESET} contains unwanted characters"

        # check the length of PW 
        elif len(user_passwrod) <= 6:
            return f'{colorama.Fore.LIGHTYELLOW_EX}your password is too short!'

        # check if PW is strong
        elif SPW != None: # return a 'strong PW' match
            # hidePW = re.sub(StrongPW, SPW.group().replace(SPW.group()[:-5], len(SPW.group()[:-5]) * '*'), SPW.group()) # LOL
            pyperclip.copy(user_passwrod)
            print(f'{colorama.Fore.GREEN}Copied to Clipboard')
            return f"{colorama.Fore.GREEN}your password '{user_passwrod}' is strong"

        else:          
            return f"{colorama.Fore.RED}your password '{user_passwrod}' is NOT strong\nbecause it's missing {colorama.Fore.MAGENTA}{explain(user_passwrod)}."

    else:
        return f"{colorama.Fore.YELLOW}No password detected"


user_input = input(f"{colorama.Fore.CYAN}please enter the password you want to check\n\
or type 'g' to generate a random password:{colorama.Fore.LIGHTMAGENTA_EX} ")

if user_input != 'g':
    print(checkPW(user_input))

else:
    print(''.center(50, '-'))
    userPW_length = int(input(f'{colorama.Fore.LIGHTYELLOW_EX}Enter the length of the password, 8 by default:{colorama.Fore.WHITE} ') or 8)
    userPW_strength = input(f'{colorama.Fore.LIGHTYELLOW_EX}choice the strength of the password\n(weak, medium, strong or very strong) strong by default:{colorama.Fore.WHITE} ') or 'strong'
    GPW = GeneratePW(userPW_length, userPW_strength)
    if userPW_strength == 'very strong':
        pyperclip.copy(GPW)
        print(f"{colorama.Fore.GREEN}'{GPW}' Copied to Clipboard ")

    else:
        print(f"Your password is '{GPW}'")