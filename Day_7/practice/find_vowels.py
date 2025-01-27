x = ['a', 'f', 'e', 'g', 'h']

x = list(filter(lambda n: n.lower() in 'aeiou', x))

print(f'Vowels: {x}')