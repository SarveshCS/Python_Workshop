# Initial values
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Logical AND
result = a and b
print("Logical AND:", result)

# Logical OR
result = a or b
print("Logical OR:", result)

# Logical NOT
result = not a
print("Logical NOT (a):", result)

result = not b
print("Logical NOT (b):", result)

# Logical AND with NOT
result = not (a and b)
print("Logical AND with NOT:", result)

# Logical OR with NOT
result = not (a or b)
print("Logical OR with NOT:", result)