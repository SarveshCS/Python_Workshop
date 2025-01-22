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

# Find a substring
find_example = example_string.find("example")
print("Find 'example':", find_example)

# Replace a substring
replace_example = example_string.replace("example", "sample")
print("Replace 'example' with 'sample':", replace_example)

# Split the string into a list of words
split_string = example_string.split()
print("Split into words:", split_string)

# Join a list of words into a string
joined_string = " ".join(split_string)
print("Joined string:", joined_string)

# Check if the string starts with a substring
starts_with_here = example_string.startswith("Here")
print("Starts with 'Here':", starts_with_here)

# Check if the string ends with a substring
ends_with_string = example_string.endswith("string")
print("Ends with 'string':", ends_with_string)

# Strip whitespace from the beginning and end
strip_whitespace = example_string.strip()
print("Strip whitespace:", strip_whitespace)

# Count occurrences of a substring
count_is = example_string.count("is")
print("Count 'is':", count_is)

# Check if the string is alphanumeric
is_alphanumeric = example_string.isalnum()
print("Is alphanumeric:", is_alphanumeric)

# Check if the string is alphabetic
is_alpha = example_string.isalpha()
print("Is alphabetic:", is_alpha)

# Check if the string is numeric
is_numeric = example_string.isnumeric()
print("Is numeric:", is_numeric)

# Check if the string is a digit
is_digit = example_string.isdigit()
print("Is digit:", is_digit)

# Check if the string is a title
is_title = example_string.istitle()
print("Is title:", is_title)

# Check if the string is in uppercase
is_upper = example_string.isupper()
print("Is uppercase:", is_upper)

# Check if the string is in lowercase
is_lower = example_string.islower()
print("Is lowercase:", is_lower)

# Check if the string is a space
is_space = example_string.isspace()
print("Is space:", is_space)