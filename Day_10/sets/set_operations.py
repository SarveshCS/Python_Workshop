set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)

# Symmetric difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)

# Checking subsets and supersets
is_subset = set_a.issubset(set_b)
print("Is set_a a subset of set_b?", is_subset)

is_superset = set_a.issuperset(set_b)
print("Is set_a a superset of set_b?", is_superset)

# Checking for disjoint sets
is_disjoint = set_a.isdisjoint(set_b)
print("Are set_a and set_b disjoint?", is_disjoint)

# Updating sets
set_a.update(set_b)
print("After updating set_a with set_b:", set_a)

set_a = {1, 2, 3}
set_a.intersection_update(set_b)
print("After intersection update of set_a with set_b:", set_a)

set_a = {1, 2, 3}
set_a.difference_update(set_b)
print("After difference update of set_a with set_b:", set_a)

set_a = {1, 2, 3}
set_a.symmetric_difference_update(set_b)
print("After symmetric difference update of set_a with set_b:", set_a)