r = int(input("Enter radius: "))
h = int(input("Enter height: "))

surface_area = (2 * 3.14 * r) * (r + h)
volume = 3.14 * (r ** 2) * h

print("Area = ", surface_area)
print("Volume = ", volume)