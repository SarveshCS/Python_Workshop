from functools import reduce
print(reduce(lambda x, y: int(x) if int(x)>int(y) else int(y), input('Enter the numbers: ').split()))