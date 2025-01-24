n = int(input('Enter number of natural numbers: '))
s = 0
t = n
while n > 0:
    s = s * 10 + n%10
    n//=10
if s==t:
    print(f"{t} is palindrome")
else:
    print(f"{t} is not palindrome")

# one liner
# print('Palindrome' if (t:=input('Enter a number: ')) == t[::-1] else 'Not a palindrome')