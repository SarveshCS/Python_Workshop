def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Floor Division")
    print("7. Modulus")

while True:
    menu()
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"\n{num1} + {num2} = {num1 + num2}\n")
        elif choice == '2':
            print(f"\n{num1} - {num2} = {num1 - num2}\n")
        elif choice == '3':
            print(f"\n{num1} * {num2} = {num1 * num2}\n")
        elif choice == '4':
            print(f"\n{num1} / {num2} = {divide(num1, num2)}\n")
        elif choice == '5':
            print(f"\n{num1} ** {num2} = {exponent(num1, num2)}\n")
        elif choice == '6':
            print(f"\n{num1} // {num2} = {floor_divide(num1, num2)}\n")
        elif choice == '7':
            print(f"\n{num1} % {num2} = {modulus(num1, num2)}\n")
    else:
        print("Invalid Input")