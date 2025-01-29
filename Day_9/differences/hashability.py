# File: /Day_9/differences/hashability.py

# Hashability in Python

# A hashable object has a hash value that remains constant during its lifetime.
# Hashable objects can be used as keys in dictionaries and as elements of sets.

# Examples of hashable types
hashable_types = {
    "int": 42,
    "float": 3.14,
    "str": "Hello",
    "tuple": (1, 2, 3),
}

# Examples of non-hashable types
non_hashable_types = {
    "list": [1, 2, 3],
    "dict": {"key": "value"},
    "set": {1, 2, 3},
}

def check_hashability(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Testing hashability
print("Hashable types:")
for name, value in hashable_types.items():
    print(f"{name}: {check_hashability(value)}")

print("\nNon-hashable types:")
for name, value in non_hashable_types.items():
    print(f"{name}: {check_hashability(value)}")