a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


if a <= b:
    if a <= c:
        greatest = c
    else:
        greatest = a
else:
    if b <= c:
        greatest = c
    else:
        greatest = b

print("The greatest number is", greatest)
