# Initial dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# Union of keys
union_keys = dict1.keys() | dict2.keys()
print("Union of keys:", union_keys)  # Output: {'a', 'b', 'c', 'd'}

# Intersection of keys
intersection_keys = dict1.keys() & dict2.keys()
print("Intersection of keys:", intersection_keys)  # Output: {'b', 'c'}

# Difference of keys
difference_keys = dict1.keys() - dict2.keys()
print("Difference of keys:", difference_keys)  # Output: {'a'}

# Symmetric difference of keys
symmetric_difference_keys = dict1.keys() ^ dict2.keys()
print("Symmetric difference of keys:", symmetric_difference_keys)  # Output: {'a', 'd'}

# Union of items
union_items = dict1.items() | dict2.items()
print("Union of items:", union_items)  # Output: {('a', 1), ('b', 2), ('b', 3), ('c', 3), ('c', 4), ('d', 5)}

# Intersection of items
intersection_items = dict1.items() & dict2.items()
print("Intersection of items:", intersection_items)  # Output: set()

# Difference of items
difference_items = dict1.items() - dict2.items()
print("Difference of items:", difference_items)  # Output: {('a', 1), ('b', 2), ('c', 3)}

# Symmetric difference of items
symmetric_difference_items = dict1.items() ^ dict2.items()
print("Symmetric difference of items:", symmetric_difference_items)  # Output: {('a', 1), ('b', 2), ('b', 3), ('c', 3), ('c', 4), ('d', 5)}

# Example dictionary for other operations
res = {'a': 1, 'b': 2, 'c': 3}

# Deleting a key-value pair
del res['b']

# Checking for the existence of a key
exists = 'a' in res

# Merging dictionaries
other_dict = {'c': 4, 'd': 5}
res.update(other_dict)

# Adding a new key-value pair
res['e'] = 6

# Accessing a value
value_c = res.get('c')

# Iterating through keys and values
for key, value in res.items():
    print(f"Key: {key}, Value: {value}")

# Final dictionary state
print(res)
print("Key 'a' exists:", exists)
print("Value of key 'c':", value_c)