a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


if a >= b:
    if a >= c:
        greatest = a
    else:
        greatest = c
else:
    if b >= c:
        greatest = b
    else:
        greatest = c

print("The greatest number is", greatest)
