# Input the lengths of the parallel sides and the height of the trapezium
a = float(input("Enter the length of the first parallel side of the trapezium: "))
b = float(input("Enter the length of the second parallel side of the trapezium: "))
height = float(input("Enter the height of the trapezium: "))

# Calculate area
area = 0.5 * (a + b) * height

print(f"The area of the trapezium is {area} square units")