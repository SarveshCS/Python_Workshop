file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'
filenames = ['file1.txt', 'file2.txt']

g = open(file_path + 'combined_file.txt', 'a')
for i in filenames:
    f = open(file_path+i)
    g.write(f.read()+'\n')
    f.close()
g.close()