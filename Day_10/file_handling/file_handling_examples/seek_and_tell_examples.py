# Sample file content for example.txt:
# Hello, World!
# This is a test file.
# It contains multiple lines of text.
# End of file.

def seek_and_tell_examples():
    with open('example.txt', 'r') as f:
        # Initial position
        print('Initial position:', f.tell())

        # Seek to 5th byte from the beginning
        f.seek(5, 0)
        print('Position after seeking to 5th byte from beginning:', f.tell())
        print('Content:', f.read(10))

        # Seek to -5th byte from the end
        f.seek(-5, 2)
        print('Position after seeking to -5th byte from end:', f.tell())
        print('Content:', f.read(5))

        # Seek to 10th byte from the current position
        f.seek(10, 1)
        print('Position after seeking to 10th byte from current position:', f.tell())
        print('Content:', f.read(10))

        # Seek to -10th byte from the current position
        f.seek(-10, 1)
        print('Position after seeking to -10th byte from current position:', f.tell())
        print('Content:', f.read(10))

        # Seek to the beginning
        f.seek(0, 0)
        print('Position after seeking to the beginning:', f.tell())
        print('Content:', f.read(10))

        # Seek to the end
        f.seek(0, 2)
        print('Position after seeking to the end:', f.tell())

if __name__ == "__main__":
    seek_and_tell_examples()