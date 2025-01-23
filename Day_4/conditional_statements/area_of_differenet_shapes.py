def area_of_circle(radius):
    return 3.14159 * radius * radius

def area_of_square(side):
    return side * side

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def main():
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
            print(f"Area of Circle: {area_of_circle(radius)}")
        elif choice == 2:
            side = float(input("Enter the side of the square: "))
            print(f"Area of Square: {area_of_square(side)}")
        elif choice == 3:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"Area of Rectangle: {area_of_rectangle(length, width)}")
        elif choice == 4:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print(f"Area of Triangle: {area_of_triangle(base, height)}")
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()