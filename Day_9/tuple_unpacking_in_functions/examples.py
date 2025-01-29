def unpack_tuple(t):
    a, b, c = t
    return a, b, c

def example_function():
    my_tuple = (1, 2, 3)
    a, b, c = unpack_tuple(my_tuple)
    print(f"Unpacked values: a={a}, b={b}, c={c}")

def multiple_return_values():
    def return_multiple():
        return 4, 5, 6
    
    x, y, z = return_multiple()
    print(f"Returned values: x={x}, y={y}, z={z}")

def unpacking_with_star():
    def func(*args):
        print("Arguments:", args)

    func(1, 2, 3, 4)

if __name__ == "__main__":
    example_function()
    multiple_return_values()
    unpacking_with_star()