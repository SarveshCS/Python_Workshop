# Example of seek(offset, whence)
with open('example.txt', 'r') as f:
    f.seek(5, 0)  # Move to the 5th byte from the beginning
    print('Seek to 5th byte from beginning:', f.read())

    f.seek(-5, 2)  # Move to the 5th byte from the end
    print('Seek to 5th byte from end:', f.read())

    f.seek(0, 1)  # Move to the current position (no change)
    print('Seek to current position:', f.read())