single_quotes = '"in principio creavit Deus caelum et terram"'
double_quotes = "'in principio creavit Deus caelum et terram'"

# allows multiple lines and retains whitespace
triple_quoted_single = '''in principio 
creavit Deus 
caelum et terram'''

# allows multiple lines and retains whitespace
triple_double_quote = """in principio 
creavit Deus 
caelum et terram"""

s = "in principio creavit Deus caelum et terram"
print(s)  # "in principio creavit Deus caelum et terram"
print(type(s))  # <class 'str'>

print("The whole string: ", s)

# String Indexing
# Print the first character wwith positive indexing
print("The furst character of s is: ", s[0])  # Returns 'i'

# Print the sixth to last character with negative indexing
print("Using Negative Indexing for the sixth to last character: ", s[-6])  # Returns 't'

# String slicing
s = "in principio creavit Deus caelum et terram"
print("\nSlicing characters from 3-12: ")
print(s[3:12])

print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(s[3:-2])


# String Methods
# str.capitalize()
# Converts the first character to uppercase and the rest to lowercase.

# str.casefold()
# Converts the string to lowercase, more aggressively than lower(). Useful for case-insensitive comparisons.

# str.center(width, [fillchar])
# Centers the string within the given width using the specified fill character (default is a space).

# str.count(substring, [start, end])
# Counts the occurrences of a substring within the specified range.

# str.encode(encoding='utf-8', errors='strict')
# Encodes the string using the specified encoding (default is UTF-8).

# str.endswith(suffix, [start, end])
# Checks if the string ends with the specified suffix.

# str.expandtabs(tabsize=8)
# Expands tabs (\t) into spaces using the specified tab size (default is 8).

# str.find(substring, [start, end])
# Returns the lowest index of the substring if found; otherwise, returns -1.

# str.format(*args, **kwargs)
# Formats the string using placeholders.

# str.format_map(mapping)
# Formats the string using a dictionary mapping.

# str.index(substring, [start, end])
# Returns the lowest index of the substring if found; raises a ValueError if not found.

# str.isalnum()
# Checks if all characters in the string are alphanumeric.

# str.isalpha()
# Checks if all characters in the string are alphabetic.

# str.isascii()
# Checks if all characters in the string are ASCII characters.

# str.isdecimal()
# Checks if all characters in the string are decimal characters (0-9).

# str.isdigit()
# Checks if all characters in the string are digits.

# str.isidentifier()
# Checks if the string is a valid Python identifier (variable name).

# str.islower()
# Checks if all characters in the string are lowercase.

# str.isnumeric()
# Checks if all characters in the string are numeric characters.

# str.isprintable()
# Checks if all characters in the string are printable.

# str.isspace()
# Checks if all characters in the string are whitespace characters.

# str.istitle()
# Checks if the string is title-cased (first character of each word is uppercase).

# str.isupper()
# Checks if all characters in the string are uppercase.

# str.join(iterable)
# Joins elements of an iterable with the string as a separator.

# str.ljust(width, [fillchar])
# Left-justifies the string within the given width using the specified fill character (default is a space).

# str.lower()
# Converts all characters in the string to lowercase.

# str.lstrip([chars])
# Removes leading characters (default is whitespace).

# str.maketrans(x, y=None, z=None)
# Creates a translation table for use with translate().

# str.partition(sep)
# Splits the string into a tuple (head, sep, tail) using the first occurrence of the separator.

# str.removeprefix(prefix) (Python 3.9+)
# Removes the specified prefix if present.

# str.removesuffix(suffix) (Python 3.9+)
# Removes the specified suffix if present.

# str.replace(old, new, [count])
# Replaces occurrences of a substring with another substring.

# str.rfind(substring, [start, end])
# Returns the highest index of the substring if found; otherwise, returns -1.

# str.rindex(substring, [start, end])
# Returns the highest index of the substring if found; raises a ValueError if not found.

# str.rjust(width, [fillchar])
# Right-justifies the string within the given width using the specified fill character (default is a space).

# str.rpartition(sep)
# Splits the string into a tuple (head, sep, tail) using the last occurrence of the separator.

# str.rsplit(sep=None, maxsplit=-1)
# Splits the string from the right using the specified separator.

# str.rstrip([chars])
# Removes trailing characters (default is whitespace).

# str.split(sep=None, maxsplit=-1)
# Splits the string using the specified separator.

# str.splitlines([keepends])
# Splits the string at line boundaries.

# str.startswith(prefix, [start, end])
# Checks if the string starts with the specified prefix.

# str.strip([chars])
# Removes leading and trailing characters (default is whitespace).

# str.swapcase()
# Swaps the case of all characters in the string (uppercase to lowercase and vice versa).

# str.title()
# Converts the first character of each word to uppercase and the rest to lowercase.

# str.translate(table)
# Translates the string using a translation table created by maketrans().

# str.upper()
# Converts all characters in the string to uppercase.

# str.zfill(width)
# Pads the string with zeros on the left to fill the specified width.