# File: /Day_9/differences/list_vs_tuple.py

# Differences between Lists and Tuples in Python

# Lists are mutable, meaning they can be changed after creation.
my_list = [1, 2, 3]
my_list[0] = 10
print("Modified List:", my_list)  # Output: Modified List: [10, 2, 3]

# Tuples are immutable, meaning they cannot be changed after creation.
my_tuple = (1, 2, 3)
# Uncommenting the next line will raise an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Performance: Tuples are generally faster than lists for iteration.
import time

# Timing list
start_time = time.time()
for _ in range(1000000):
    _ = [1, 2, 3]
print("List time:", time.time() - start_time)

# Timing tuple
start_time = time.time()
for _ in range(1000000):
    _ = (1, 2, 3)
print("Tuple time:", time.time() - start_time)

# Use cases: Lists are used for collections of items that may change, while tuples are used for fixed collections of items.
list_example = [1, 2, 3, 4]
tuple_example = (1, 2, 3, 4)

print("List Example:", list_example)
print("Tuple Example:", tuple_example)