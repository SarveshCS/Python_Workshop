def handle_file_operations(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(f"File '{file_path}' read successfully.")
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result of division: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

def main():
    # Example of handling file operations
    handle_file_operations('example.txt')

    # Example of handling division
    divide_numbers(10, 0)

if __name__ == "__main__":
    main()