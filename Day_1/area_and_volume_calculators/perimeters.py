# Day_1/area_and_volume_calculators/perimeters.py
import math

# Perimeter of Circle
radius = float(input("Enter the radius of the circle: "))
circle_perimeter = 2 * math.pi * radius
print("Perimeter of the circle is:", circle_perimeter)

# Perimeter of Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_perimeter = 2 * (length + width)
print("Perimeter of the rectangle is:", rectangle_perimeter)

# Perimeter of Triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
triangle_perimeter = a + b + c
print("Perimeter of the triangle is:", triangle_perimeter)