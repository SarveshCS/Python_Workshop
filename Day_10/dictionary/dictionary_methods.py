sample_dict = {'a': 1, 'b': 2, 'c': 3}

# Example of get()
print(sample_dict.get('d', 'Not Found'))  # Output: Not Found

# Example of keys()
print(sample_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# Example of values()
print(sample_dict.values())  # Output: dict_values([1, 2, 3])

# Example of items()
print(sample_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Example of pop()
removed_value = sample_dict.pop('b')  # Removes key 'b'
print(removed_value)  # Output: 2
print(sample_dict)  # Output: {'a': 1, 'c': 3}

# Example of update()
sample_dict.update({'d': 4, 'e': 5})
print(sample_dict)  # Output: {'a': 1, 'c': 3, 'd': 4, 'e': 5}

# Example of adding a key-value pair using assignment
sample_dict['f'] = 6
print(sample_dict)  # Output: {'a': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Example of deleting a key-value pair using del
del sample_dict['a']
print(sample_dict)  # Output: {'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Example of checking if a key exists using 'in'
print('c' in sample_dict)  # Output: True
print('a' in sample_dict)  # Output: False

# Example of iterating over keys
for key in sample_dict:
    print(key, sample_dict[key])
# Output:
# c 3
# d 4
# e 5
# f 6

# Example of dictionary comprehension
squared_dict = {k: v**2 for k, v in sample_dict.items()}
print(squared_dict)  # Output: {'c': 9, 'd': 16, 'e': 25, 'f': 36}

# Example of merging dictionaries using |
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Example of intersecting dictionaries using &
dict3 = {'a': 1, 'b': 2, 'c': 3}
dict4 = {'b': 2, 'c': 4, 'd': 5}
intersection_dict = {k: dict3[k] for k in dict3.keys() & dict4.keys()}
print(intersection_dict)  # Output: {'b': 2, 'c': 3}