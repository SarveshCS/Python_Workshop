res = {}

# Example of fromkeys()
keys = ['a', 'b', 'c']
default_value = 0
res_fromkeys = dict.fromkeys(keys, default_value)
print("fromkeys:", res_fromkeys)

# Example of setdefault()
sample_dict = {'x': 1, 'y': 2}
value = sample_dict.setdefault('z', 3)
print("setdefault:", sample_dict)  # 'z' is added with value 3

# Example of copy()
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()
print("copy:", copied_dict)  # copied_dict is a shallow copy of original_dict

# Example of popitem()
popped_item = original_dict.popitem()
print("popitem:", popped_item)  # removes and returns the last inserted key-value pair

# Example of clear()
sample_dict.clear()
print("clear:", sample_dict)  # sample_dict is now empty