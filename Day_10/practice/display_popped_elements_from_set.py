data = set(input('Enter set elements: ').split())

res = [data.pop() for i in range(len(data))]

print(res)