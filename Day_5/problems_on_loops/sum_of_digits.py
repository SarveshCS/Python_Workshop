n = int(input('Enter number of natural numbers: '))
s = 0
while n > 0:
    s += n%10
    n//=10
print(s)

# one liner
# print(sum([int(i) for i in input('Enter the number: ')]))