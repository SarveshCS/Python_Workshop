def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    x = fib(n-1) + fib(n-2)
    return x

n = int(input('Enter a number: '))
for i in range(n):
    print(fib(i+1), end=' ')