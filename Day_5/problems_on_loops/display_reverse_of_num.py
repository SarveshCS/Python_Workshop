n = int(input('Enter number of natural numbers: '))
s = 0
while n > 0:
    s = s * 10 + n%10
    n//=10
print(s)
