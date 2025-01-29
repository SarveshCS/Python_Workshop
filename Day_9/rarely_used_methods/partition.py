# File: /Day_9/rarely_used_methods/partition.py

# Demonstrating the use of the partition() method for strings

def demonstrate_partition():
    example_string = "Hello, welcome to the world of Python!"
    
    # Using partition to split the string at the first occurrence of a substring
    before, separator, after = example_string.partition("welcome")
    
    print("Original String:", example_string)
    print("Before Separator:", before)
    print("Separator:", separator)
    print("After Separator:", after)

if __name__ == "__main__":
    demonstrate_partition()