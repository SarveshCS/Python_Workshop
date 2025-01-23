while True:
    print("Choose the shape to calculate the area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of Circle: {3.14159 * radius * radius}")
    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        print(f"Area of Square: {side * side}")
    elif choice == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area of Rectangle: {length * width}")
    elif choice == 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of Triangle: {0.5 * base * height}")
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
