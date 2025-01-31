def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of '{file_path}':\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_path}' successfully.")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            print(f"Content appended to '{file_path}' successfully.")
    except IOError as e:
        print(f"Error appending to file '{file_path}': {e}")

def main():
    test_file = 'example.txt'
    
    write_file(test_file, 'Hello, World!')
    read_file(test_file)
    append_to_file(test_file, '\nAppending this line.')
    read_file(test_file)

if __name__ == "__main__":
    main()