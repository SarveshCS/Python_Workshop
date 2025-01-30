# Example of tell()
with open('example.txt', 'r') as f:
    print('Current file position:', f.tell())

# Example of flush()
with open('example.txt', 'w') as f:
    f.write('Hello, World!')
    f.flush()  # Ensure data is written to disk

# Example of truncate(size)
with open('example.txt', 'w') as f:
    f.write('Hello, World!')
    f.truncate(5)  # Truncate file to 5 bytes

# Example of fileno()
with open('example.txt', 'r') as f:
    print('File descriptor:', f.fileno())

# Example of isatty()
with open('example.txt', 'r') as f:
    print('Is a terminal device:', f.isatty())

# Example of readable()
with open('example.txt', 'r') as f:
    print('Is readable:', f.readable())

# Example of writable()
with open('example.txt', 'w') as f:
    print('Is writable:', f.writable())

# Example of seekable()
with open('example.txt', 'r') as f:
    print('Is seekable:', f.seekable())