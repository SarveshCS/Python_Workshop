# Creating a set
my_set = {1, 2, 3}
print("Initial set:", my_set)

# Adding elements
my_set.add(4)
print("After adding 4:", my_set)

# Removing elements
my_set.remove(3)  # Raises KeyError if element is not found
print("After removing 3:", my_set)

my_set.discard(2)  # Does not raise an error if element is not found
print("After discarding 2:", my_set)

# Removing and returning an arbitrary element
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After popping an element:", my_set)

# Clearing the set
my_set.clear()
print("After clearing the set:", my_set)