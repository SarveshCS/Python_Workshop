from functools import reduce
print(reduce(lambda x, y: int(x)+int(y), input('Enter the numbers: ').split()))