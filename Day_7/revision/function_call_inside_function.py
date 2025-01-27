def func1():
    def func2():
        return 'Hello'
    return func2
x = func1()()
print(x)