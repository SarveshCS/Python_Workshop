from functools import reduce

def sum_of_list(numbers):
    return reduce(lambda x, y: int(x) + int(y), numbers)