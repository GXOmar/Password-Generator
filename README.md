# ***isPW_strong***
This Program is a text based (CLI) experience to Generate a Random password for the user.<br>
It could also check if the password is strong or not from a user input.<br>

This is the first program "as a Beginner" that i did. 
I was following an amazing book by **Al Sweigart** called **"AUTOMATE THE BORING STUFF WITH PYTHON"** Chapter 7: Pattern Matching with Regular Expressions. _page 171_<br>
he asked to write a program for Strong Password Detection and the idea was to use Regex pattern to check the password contain the following:
* at least 8 characters long.
* at least 1 upper case letter.
* at least 1 lower case letter.
* at least 1 digit.
* at least 1 symbol.

#### It was a simple task but it took me a while to figure out how "Look around" mechanism work in regex.<br>
Thanks to this [Regex Debugger tool](https://regex101.com/) that showed me how the mechanism work step by step.<br> 
*"it was at that moment I knew, it makes sense" :sweat_smile:*<br>

## The program was just to check if the password strong or not.<br>
### what inspired me to keep developing it and make it my first project is [LastPass](https://www.lastpass.com/) Generate Secure Password tab in the [chrome extension](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?utm_source=chrome-ntp-icon).
which I'll keep developing this program to somewhat match the chrome extension.<br>
**___________________________________________________________________**<br>
_Also_, I don't know what kind of symbols allowed in a password, so i only allowed the following symbols 
  * **!?@#$%^&\***
  
_"Various operating systems and applications may apply limitations to this set"_ >>> **!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~**<br>
e.g. windows 7 doesn't allow **"\\/:*?"<>|"** these characters when renaming a folder or file 

**any ideas or advice are more than welcome** :hugs: 
