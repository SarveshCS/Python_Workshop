n = int(input('Enter a number: '))
t = n
number_of_digits = 0
s = 0
while n > 0:
    n//=10
    number_of_digits += 1

n = t
while n > 0:
    s += (n%10)**number_of_digits
    n//=10


if s == t:
    print(f'{s} is armstrong')
else:
    print(f'{t} is not armstrong')