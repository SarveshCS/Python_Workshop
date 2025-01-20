a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Using the .format() method to insert variables into the string
print("The first number is {} and the second number is {}.".format(a, b))

# Using index numbers in the .format() method to specify the position of variables
print("The first number is {0} and the second number is {1}.".format(a, b))

# Using keyword arguments in the .format() method to specify the variables
print("The first number is {first} and the second number is {second}.".format(first = a, second = b))