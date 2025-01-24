n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))
 
fact = 1
for i in range(2, r + 1):
    fact *= i
nval = fact
 
fact = 1
for i in range(2, r + 1):
    fact *= i
rval = fact
 
fact = 1
for i in range(2, (n-r) + 1):
    fact *= i
nrval = fact
 
nCr = nval // (rval * nrval)
 
print(f"The value of {n}C{r} is: {nCr}")
