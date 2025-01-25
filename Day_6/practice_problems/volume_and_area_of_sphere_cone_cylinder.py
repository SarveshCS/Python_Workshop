def sphere():
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * 3.14 * radius**3
    surface_area = 4 * 3.14 * radius**2
    print(f"Volume of the sphere: {volume}")
    print(f"Surface area of the sphere: {surface_area}")

def cone():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1/3) * 3.14 * radius**2 * height
    slant_height = (radius**2 + height**2)**0.5
    surface_area = 3.14 * radius * (radius + slant_height)
    print(f"Volume of the cone: {volume}")
    print(f"Surface area of the cone: {surface_area}")

def cylinder():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = 3.14 * radius**2 * height
    surface_area = 2 * 3.14 * radius * (radius + height)
    print(f"Volume of the cylinder: {volume}")
    print(f"Surface area of the cylinder: {surface_area}")

def main():
    print("Which calculations do you want to choose: \n1. Sphere\n2. Cone\n3. Cylinder")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        sphere()
    elif choice == 2:
        cone()
    elif choice == 3:
        cylinder()
    else:
        print("Invalid choice")

main()