lst = [2, 9, 4, 6, 8, 1, 4, 8, 54, 85,5, 5]

print(lst[-5:-10:-1])
print(lst[::])
print(lst[:])
print(lst[::-1])

a = slice(2, 5, 2)
print(lst[a])

# Using slice object literally
start, stop, step = a.indices(len(lst))
sliced_list = [lst[i] for i in range(start, stop, step)]
print(sliced_list)
sliced_list = lst[start:stop:step]
print(sliced_list)