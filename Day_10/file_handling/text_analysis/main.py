file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'


f = open(file_path + 'file.txt', 'r')
char_count = len(f.read())
f.seek(0)
word_count = len(f.read().split(' '))
f.seek(0)
line_count = len(f.readlines())
f.close()

print(f'Characters: {char_count}\nWords: {word_count}\nLines: {line_count}')