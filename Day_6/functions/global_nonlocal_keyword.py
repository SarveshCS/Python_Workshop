# Example to demonstrate the use of global and nonlocal keywords

# Global variable
x = "global_x"

def outer_function():
    # Enclosing variable
    x = "outer_x"
    
    def inner_function():
        nonlocal x  # This will refer to the x in the outer_function scope
        x = "inner_x"
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()
print("Global scope:", x)

def global_example():
    global y
    y = "global_y"

global_example()
print("Global variable y:", y)