# File: /Day_9/nested_loops/examples.py

# Example 1: Generating a pattern using nested loops
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

# Example 2: Multiplication table using nested loops
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i * j:4}', end=' ')
    print()

# Example 3: Processing a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value, end=' ')
    print()

# Example 4: Nested loops with condition
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()