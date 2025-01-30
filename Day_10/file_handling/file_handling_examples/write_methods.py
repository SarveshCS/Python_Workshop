# Example of write(string)
with open('example.txt', 'w') as f:
    f.write('Hello, World!')

# Example of writelines(lines)
with open('example.txt', 'w') as f:
    f.writelines(['Hello, World!\n', 'This is a test.\n'])