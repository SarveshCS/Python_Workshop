from functools import reduce
print(list(reduce(lambda x, y: x if x>y else y, input('Enter the numbers: ').split())))