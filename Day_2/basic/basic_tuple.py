import sys
a = (2, 24.42, "RAM", [5, 7, 8])
print(a, str(type(a)).split('\'')[1])


# Tuple is immutable but any mutable elements inside it can be accsed and mutated
a[-1][1] = 100


b = [2, 24.42, "RAM", [5, 7, 8]]
print(a)

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))