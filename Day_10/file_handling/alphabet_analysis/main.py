file_path = __file__[::-1].partition('\\')[-1][::-1]+'\\'


f = open(file_path + 'text_to_analyse.txt', 'r')
data = f.read()
f.close()


vowel_count = 0
consonant_count = 0

for i in data:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowel_count+=1
        else:
            consonant_count+=1


print(f'Vowels: {vowel_count}\nConsonants: {consonant_count}')