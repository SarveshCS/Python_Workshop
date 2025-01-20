# Day_1/area_and_volume_calculators/cuboid_area_volume.py
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

surface_area = 2 * (length * width + width * height + height * length)
volume = length * width * height

print("Surface area of the cuboid is:", surface_area)
print("Volume of the cuboid is:", volume)