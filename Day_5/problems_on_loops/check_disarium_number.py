n = int(input('Enter a number: '))
t = n
s = 0
i = 1
d = 0
while n > 0:
    s = s * 10 + n%10
    n//=10

while s > 0:
    d += (s%10)**i
    s//=10
    i+=1
if d == t:
    print(f'{t} is Disarium number')
else:
    print(f'{t} is not Disarium number')