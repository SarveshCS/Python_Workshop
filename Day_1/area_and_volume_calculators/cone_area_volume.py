r = int(input("Enter radius: "))
l = int(input("Enter slant height: "))
h = int(input("Enter height: "))

surface_area = 3.14 * r * (r + l)
volume = (1/3) * 3.14 * (r ** 2) * h

print("Area = ", surface_area)
print("Volume = ", volume)