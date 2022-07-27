# **myPassword.py**

Password generator and validator

This program is a text-based experience to generate a random password for the user, and validate a password from user input.

Usage: `py myPassword.py <command_keyword>`

`<command_keyword>` includes:

* "gen": Generate a strong password, 20 characters long (default)
  * optional argument for password length. example: py myPassword.py gen 77

* "check": Validate if the password is strong or not, user will be prompt to enter the password.  

___

###### This is the first program that I wrote. ^_^

I was following an amazing book by **Al Sweigart** called **"AUTOMATE THE BORING STUFF WITH PYTHON"** Chapter 7: Pattern Matching with Regular Expressions. page 171

He asked to write a program for strong password detection and the idea was to use Regex pattern to check the password contains the following:

* At least 8 characters long.
* At least 1 uppercase character.
* At least 1 lowercase character.
* At least 1 digit.
* At least 1 symbol.

The program was just to check if the password strong or not

### what inspired me to keep developing it is the [LastPass...](https://www.lastpass.com/) Generate Secure Password tab in the [chrome extension](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?utm_source=chrome-ntp-icon)

___

Note: I only allowed the following symbols in the password generating/checking process:

* **!?@#$%^&\***

Various operating systems and applications may apply limitations to what kind of symbols they might want to use, so i choose to not have these symbols when generating/checking the password.

* **\[ \]\( \):;,~.`\'\"/+=\\-_<>{ }**

e.g. Windows 10 doesn't allow these characters **"\\/:*?"<>|"** when renaming a folder or a file.

**any ideas or advice are more than welcome** :hugs:
