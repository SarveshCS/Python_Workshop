### Day 9 Python Workshop Folder Structure

```
Day_9_Python_Workshop/
│
├── Packing_Unpacking/
│   ├── nested_unpacking.py
│   ├── extra_values_unpacking.py
│   └── dictionary_merging.py
│
├── Mutable_vs_Immutable/
│   ├── mutable_vs_immutable.py
│   ├── hashability_examples.py
│   └── memory_optimization.py
│
├── Advanced_Strings/
│   ├── translate_method.py
│   ├── partition_method.py
│   └── encoding_error_handling.py
│
├── Lists_and_Comprehensions/
│   ├── nested_loops.py
│   ├── walrus_operator.py
│   └── modifying_lists_during_iteration.py
│
├── Tuples/
│   ├── single_element_syntax.py
│   ├── namedtuple_example.py
│   └── tuple_unpacking.py
│
└── Practice_Problems/
    ├── unpacking_challenges.py
    ├── string_translation_problems.py
    └── comprehension_edge_cases.py
```

### Example Content for Each File

#### Packing_Unpacking/nested_unpacking.py
```python
# Nested Unpacking Example
data = (1, (2, 3), 4)
a, (b, c), d = data
print(a, b, c, d)  # Output: 1 2 3 4
```

#### Packing_Unpacking/extra_values_unpacking.py
```python
# Unpacking with * for extra values
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)  # Output: 1 [2, 3, 4] 5
```

#### Packing_Unpacking/dictionary_merging.py
```python
# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

#### Mutable_vs_Immutable/mutable_vs_immutable.py
```python
# Mutable vs Immutable
my_list = [1, 2, 3]  # Mutable
my_tuple = (1, 2, 3)  # Immutable
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# my_tuple.append(4)  # This would raise an AttributeError
```

#### Mutable_vs_Immutable/hashability_examples.py
```python
# Hashability Example
print(hash((1, 2, 3)))  # Output: Hash value
# print(hash([1, 2, 3]))  # This would raise a TypeError
```

#### Mutable_vs_Immutable/memory_optimization.py
```python
# Memory Optimization Example
import sys

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(sys.getsizeof(my_list))  # Output: Size in bytes
print(sys.getsizeof(my_tuple))  # Output: Size in bytes
```

#### Advanced_Strings/translate_method.py
```python
# Using translate() method
translation_table = str.maketrans("abc", "123")
translated = "abcde".translate(translation_table)
print(translated)  # Output: 123de
```

#### Advanced_Strings/partition_method.py
```python
# Using partition() method
s = "Hello, World!"
before, sep, after = s.partition(", ")
print(before, sep, after)  # Output: Hello  ,  World!
```

#### Advanced_Strings/encoding_error_handling.py
```python
# Encoding Error Handling
try:
    b = bytes("Hello", "ascii")
    print(b)
    b = bytes("Hello", "ascii", errors="strict")  # Default
except UnicodeEncodeError as e:
    print(e)
```

#### Lists_and_Comprehensions/nested_loops.py
```python
# Nested Loops Example
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
```

#### Lists_and_Comprehensions/walrus_operator.py
```python
# Using Walrus Operator
if (n := len([1, 2, 3, 4])) > 3:
    print(f"List has {n} elements.")  # Output: List has 4 elements.
```

#### Lists_and_Comprehensions/modifying_lists_during_iteration.py
```python
# Modifying Lists During Iteration
my_list = [1, 2, 3, 4]
for i in my_list:
    my_list.remove(i)  # This can lead to unexpected behavior
print(my_list)  # Output: [2, 4]
```

#### Tuples/single_element_syntax.py
```python
# Single Element Tuple Syntax
single_element_tuple = (1,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
```

#### Tuples/namedtuple_example.py
```python
# Using namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
```

#### Tuples/tuple_unpacking.py
```python
# Tuple Unpacking in Functions
def return_tuple():
    return (1, 2)

a, b = return_tuple()
print(a, b)  # Output: 1 2
```

#### Practice_Problems/unpacking_challenges.py
```python
# Unpacking Challenges
data = (1, 2, (3, 4))
a, b, (c, d) = data
print(a, b, c, d)  # Output: 1 2 3 4
```

#### Practice_Problems/string_translation_problems.py
```python
# String Translation Problems
def translate_string(s):
    translation_table = str.maketrans("xyz", "123")
    return s.translate(translation_table)

print(translate_string("xyzabc"))  # Output: 123abc
```

#### Practice_Problems/comprehension_edge_cases.py
```python
# Comprehension Edge Cases
# Example of a pitfall
my_list = [1, 2, 3, 4]
squared = [x**2 for x in my_list if x > 2]
print(squared)  # Output: [9, 16]
```

### Conclusion
This folder structure and example content will help you organize your workshop materials effectively, making it easier for participants to navigate through the topics and understand the concepts with practical examples.