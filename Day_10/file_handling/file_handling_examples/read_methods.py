# Example of read(size)
with open('example.txt', 'r') as f:
    content = f.read(10)  # Reads the first 10 bytes
    print('Read 10 bytes:', content)

# Example of readline(size)
with open('example.txt', 'r') as f:
    line = f.readline()  # Reads the first line
    print('Read one line:', line)

# Example of readlines(hint)
with open('example.txt', 'r') as f:
    lines = f.readlines()  # Reads all lines
    print('Read all lines:', lines)