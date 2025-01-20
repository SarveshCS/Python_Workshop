a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swap a, b : ", a, b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swap a, b  : ", a, b)