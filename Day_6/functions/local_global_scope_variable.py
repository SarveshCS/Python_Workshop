# Global variable
global_var = "I am a global variable"

def example_function():
    # Local variable
    local_var = "I am a local variable"
    
    print(local_var)  # This will work because local_var is defined within this function
    
    # Trying to modify a global variable without declaring it as global
    global_var = "Trying to modify global variable"  # This will create a new local variable instead of modifying the global one

    print(global_var)  # This will print the local variable, not the global one

def correct_example_function():
    global global_var  # Declare that we want to use the global variable
    global_var = "I am modifying the global variable"
    
    print(global_var)  # This will print the modified global variable

example_function()
print(global_var)  # This will print the original global variable because it was not modified in example_function

correct_example_function()
print(global_var)  # This will print the modified global variable