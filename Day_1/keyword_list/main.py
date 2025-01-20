import keyword

print("Keyword list: ")
print(*[str(i+1) + " -> " + str(key).strip()+"\n" for i, key in enumerate(keyword.kwlist)])