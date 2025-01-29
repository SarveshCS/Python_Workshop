# File: /Day_9/walrus_operator/examples.py

# Example of using the walrus operator (:=) for assignment expressions

# Using walrus operator in a while loop
data = []
while (user_input := input("Enter a value (or 'quit' to exit): ")) != 'quit':
    data.append(user_input)

print("Collected data:", data)

# Using walrus operator in a list comprehension
squared = [num := x**2 for x in range(10)]
print("Squared values:", squared)

# Using walrus operator to simplify an if statement
if (length := len(data)) > 0:
    print(f"You entered {length} values.")
else:
    print("No values were entered.")