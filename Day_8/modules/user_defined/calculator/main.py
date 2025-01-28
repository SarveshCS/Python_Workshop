from operations import sum_of_list, add, sub, mul, div, pow

numbers = input('Enter the numbers separated by space: ').split()
print(f"The sum of the list is: {sum_of_list(numbers)}")

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print(f"The addition of {a} and {b} is: {add(a, b)}")
print(f"The subtraction of {b} from {a} is: {sub(a, b)}")
print(f"The multiplication of {a} and {b} is: {mul(a, b)}")
try:
    print(f"The division of {a} by {b} is: {div(a, b)}")
except ValueError as e:
    print(e)
print(f"The power of {a} raised to {b} is: {pow(a, b)}")