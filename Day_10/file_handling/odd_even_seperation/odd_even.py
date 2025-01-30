file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'

n = int(input('Enter a number: '))

f = open(file_path+'odd.txt', 'a')
g = open(file_path+'even.txt', 'a')


if n%2:
    f.write(f'{n}\n')
else:
    g.write(f'{n}\n')

f.close()
g.close()