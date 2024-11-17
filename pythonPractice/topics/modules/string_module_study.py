import string

# https://github.com/python/cpython/blob/3.12/Lib/string.py
# String Constants
print(f"string.ascii_lettres: {string.ascii_letters}")  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"string.ascii_lowercase: {string.ascii_lowercase}")  # abcdefghijklmnopqrstuvwxyz
print(f"string.ascii_uppercase: {string.ascii_uppercase}")  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"string.digits: {string.digits}")  # 0123456789
print(f"string.hexdigits: {string.hexdigits}")  # 0123456789abcdefABCDEF
print(f"string.octdigits: {string.octdigits}")  # 01234567
print(f"string.punctuation: {string.punctuation}")  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(f"string.printable: {string.printable}")  # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(f"string.whitespace: {string.whitespace}")  # space, tab, linefeed, return, formfeed, and vertical tab.


# Check to see if a character is in the string.printable constant
def is_character_printable(char):
    return char in string.printable

print(is_character_printable('A'))  # True
print(is_character_printable('\t'))  # True (tab is printable)
print(is_character_printable('\x07'))  # False (bell character is not printable)