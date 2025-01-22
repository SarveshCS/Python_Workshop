# Define the string
example_string = "Here is an example string"

# Convert to uppercase
upper_case = example_string.upper()
print("Uppercase:", upper_case)

# Convert to lowercase
lower_case = example_string.lower()
print("Lowercase:", lower_case)

# Capitalize the first letter
capitalized = example_string.capitalize()
print("Capitalized:", capitalized)

# Title case (capitalize the first letter of each word)
title_case = example_string.title()
print("Title Case:", title_case)

# Swap case (uppercase to lowercase and vice versa)
swap_case = example_string.swapcase()
print("Swap Case:", swap_case)

# Casefold (more aggressive lowercasing)
casefolded = example_string.casefold()
print("Casefold:", casefolded)

# Center the string with a specified width
centered = example_string.center(40, '-')
print("Centered:", centered)

# Count occurrences of a substring
count = example_string.count('e')
print("Count of 'e':", count)

# Check if the string ends with a specific suffix
ends_with = example_string.endswith('string')
print("Ends with 'string':", ends_with)

# Find the position of a substring
find_pos = example_string.find('example')
print("Find 'example':", find_pos)

# Replace a substring with another substring
replaced = example_string.replace('example', 'sample')
print("Replaced 'example' with 'sample':", replaced)

# Check if the string starts with a specific prefix
starts_with = example_string.startswith('Here')
print("Starts with 'Here':", starts_with)

# Encode the string to bytes
encoded = example_string.encode()
print("Encoded:", encoded)

# Check if the string is alphanumeric
is_alnum = example_string.isalnum()
print("Is Alphanumeric:", is_alnum)

# Check if the string is alphabetic
is_alpha = example_string.isalpha()
print("Is Alphabetic:", is_alpha)

# Check if the string is ASCII
is_ascii = example_string.isascii()
print("Is ASCII:", is_ascii)

# Check if the string is a digit
is_digit = example_string.isdigit()
print("Is Digit:", is_digit)

# Check if the string is a valid identifier
is_identifier = example_string.isidentifier()
print("Is Identifier:", is_identifier)

# Check if the string is in lowercase
is_lower = example_string.islower()
print("Is Lowercase:", is_lower)

# Check if the string is numeric
is_numeric = example_string.isnumeric()
print("Is Numeric:", is_numeric)

# Check if the string is printable
is_printable = example_string.isprintable()
print("Is Printable:", is_printable)

# Check if the string is in title case
is_title = example_string.istitle()
print("Is Title Case:", is_title)

# Check if the string is in uppercase
is_upper = example_string.isupper()
print("Is Uppercase:", is_upper)

# Join elements of an iterable with the string as separator
joined = '-'.join(['Here', 'is', 'an', 'example', 'string'])
print("Joined:", joined)

# Left justify the string with a specified width
left_justified = example_string.ljust(40, '-')
print("Left Justified:", left_justified)

# Right justify the string with a specified width
right_justified = example_string.rjust(40, '-')
print("Right Justified:", right_justified)

# Strip leading whitespace
left_stripped = example_string.lstrip()
print("Left Stripped:", left_stripped)

# Strip trailing whitespace
right_stripped = example_string.rstrip()
print("Right Stripped:", right_stripped)

# Strip leading and trailing whitespace
stripped = example_string.strip()
print("Stripped:", stripped)

# Partition the string into three parts
partitioned = example_string.partition('example')
print("Partitioned:", partitioned)

# Split the string at line breaks
split_lines = example_string.splitlines()
print("Split Lines:", split_lines)

# Split the string into a list
split = example_string.split()
print("Split:", split)

# Right partition the string into three parts
rpartitioned = example_string.rpartition('example')
print("Right Partitioned:", rpartitioned)

# Right split the string into a list
rsplit = example_string.rsplit()
print("Right Split:", rsplit)

# Zero fill the string with a specified width
zero_filled = example_string.zfill(40)
print("Zero Filled:", zero_filled)

# Translate the string using a translation table
translation_table = str.maketrans('aeiou', '12345')
translated = example_string.translate(translation_table)
print("Translated:", translated)

# Format the string
formatted = "This is an {0}".format('example')
print("Formatted:", formatted)

# Concatenate strings using dunder method
concatenated = example_string.__add__(' concatenated')
print("Concatenated:", concatenated)

# Multiply string using dunder method
multiplied = example_string.__mul__(3)
print("Multiplied:", multiplied)