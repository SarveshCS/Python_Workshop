# Set comprehensions
squared_set = {x**2 for x in range(10)}
print("Set of squares from 0 to 9:", squared_set)

even_set = {x for x in range(10) if x % 2 == 0}
print("Set of even numbers from 0 to 9:", even_set)