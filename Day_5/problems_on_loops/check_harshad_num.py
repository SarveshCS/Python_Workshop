n = int(input('Enter a number: '))
t = n
i = 1
s = 0
while n > 0:
    s += n%10
    n//=10

if t%s == 0:
    print(f'{t} is Harshad number')
else:
    print(f'{t} is not Harshad number')