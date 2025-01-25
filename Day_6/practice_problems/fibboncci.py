n = int(input('Enter a number: '))

def fibb(n):
    i, a, b = 0, 0, 1
    while i<n:
        # print(a)
        b = a+b
        a = b-a
        i+=1
    return a
print(fibb(n))