a, b, c = list(map(int, input('Enter the value of a, b, c: ').split()))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Function to calculate square root using Newton's method
def sqrt(n):
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x

# Check the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    print(f'The roots are real and different: {root1} and {root2}')
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f'The root is real and repeated: {root}')
else:
    # Two complex roots
    real_part = -b / (2*a)
    imaginary_part = sqrt(-discriminant) / (2*a)
    print(f'The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i')