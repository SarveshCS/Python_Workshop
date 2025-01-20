a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

p = (a+b+c)/2
area = (p*(p-1)*(p-b)*(p-c)) ** 0.5

print("Area =", area)