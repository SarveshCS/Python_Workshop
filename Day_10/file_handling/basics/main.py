file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'

filename = 'CSE-001.txt'

file = file_path + filename

with open(file, 'a') as f:
    data = f.read()
    print(data)