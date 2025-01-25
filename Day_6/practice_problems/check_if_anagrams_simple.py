str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

def checkAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

if checkAnagram(str1.lower(), str2.lower()):
    print('yes they are anagrams')
else:
    print('No they are not anagrams')