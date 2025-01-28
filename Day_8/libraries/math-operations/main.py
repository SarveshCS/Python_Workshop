# File: /my-python-library/my-python-library/main.py

from math_operations import add_numbers, multiply_numbers, greet, calculate_square

def main():
    # Demonstrate the usage of functions from the library
    sum_result = add_numbers(5, 3)
    product_result = multiply_numbers(4, 2)
    greeting = greet("Alice")
    square_result = calculate_square(6)

    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")
    print(greeting)
    print(f"Square: {square_result}")

if __name__ == "__main__":
    main()