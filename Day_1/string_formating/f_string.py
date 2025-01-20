a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Using the f string we can directly place the variables in the desired places in between {}
print(f"The first number is {a} and the second number is {b}.")

# When we use a '=' after the variable name in the {} it prints the variable name and then the value (ie: a=5)
print(f"The first number is {a=} and the second number is {b=}.")

# This is one the ways to format string in python, we will see more of these 'tricks' in the later commit