n = int(input('Enter a number: '))
for i in range(0, n):
    for j in range(i):
        print(chr(i+ord('A')), end=" ")
    print()