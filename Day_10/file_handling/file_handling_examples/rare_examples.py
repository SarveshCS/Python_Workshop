# Example of detach()
import io

with open('example.txt', 'rb') as f:
    buffer = f.detach()
    print('Detached buffer:', buffer)

# Example of readinto(b)
with open('example.txt', 'rb') as f:
    b = bytearray(10)
    f.readinto(b)
    print('Read into bytearray:', b)