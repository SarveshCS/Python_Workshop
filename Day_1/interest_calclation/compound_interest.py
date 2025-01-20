p = int(input("Enter principle amount: "))
r = int(input("Enter rate: "))
n = int(input("Enter n: "))

a = (p * (1 - r/100)) ** n
ci = a-p

print("Compound interest = ", ci)