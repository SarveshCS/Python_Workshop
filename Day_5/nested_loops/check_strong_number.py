n = int(input("Enter number: "))
t = n

i = 1
s = 0
while n > 0:
    rem = n%10
    fact = 1
    for i in range(1, rem+1):
        fact*=i
    s += fact
    n//=10

if t == s:
    print(f'{t} is a strong number')
else:
    print(f'{t} is not a strong number')
