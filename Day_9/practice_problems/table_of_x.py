x = int(input('Enter a number: '))

print('\n'.join([f'{x} x {i} = {i*x}' for i in range(1, 11)]))