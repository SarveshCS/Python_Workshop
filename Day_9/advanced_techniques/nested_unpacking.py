# File: /Day_9/advanced_techniques/nested_unpacking.py

# Demonstrating nested unpacking in Python

# Example of nested unpacking with a tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
(a, b), (c, d), (e, f) = nested_tuple

print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}")

# Example of nested unpacking with a list
nested_list = [[1, 2], [3, 4], [5, 6]]
[x, y], [z, w], [u, v] = nested_list

print(f"x: {x}, y: {y}, z: {z}, w: {w}, u: {u}, v: {v}")

# Example of unpacking with a mix of lists and tuples
mixed_structure = [((1, 2), 3), ((4, 5), 6)]
((a1, a2), b1), ((c1, c2), b2) = mixed_structure

print(f"a1: {a1}, a2: {a2}, b1: {b1}, c1: {c1}, c2: {c2}, b2: {b2}")