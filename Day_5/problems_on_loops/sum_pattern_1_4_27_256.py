i = 1
n = int(input('Enter number of natural numbers: '))
s = 0
while i<=n:
    s += i**i
    i+=1
print("sum:", s)