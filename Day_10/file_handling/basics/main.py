file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'
filename = file_path + 'CSE-001.txt'

f = open(filename, 'r')
print(f.read())

f.close()