n = int(input('Enter n: '))
r = int(input('Enter r: '))

if r > n:
    print(0)
else:
    if r > n - r:
        r = n - r

    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)

    print(f'nCr({n}, {r}) = {c}')