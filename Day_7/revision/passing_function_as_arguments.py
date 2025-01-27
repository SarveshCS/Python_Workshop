def one(n):
    return n + ' 1'
def two(n):
    return n + ' 2'
def three(x):
    x1 = x('Inside function')
    print(x1)
three(one)
three(two)