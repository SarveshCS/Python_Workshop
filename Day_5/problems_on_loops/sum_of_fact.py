i = 1
n = int(input('Enter number of natural numbers: '))
fact = 1
s = 0
while i<=n:
    fact*=i
    s += fact
    i+=1
print("sum of fact:", s)