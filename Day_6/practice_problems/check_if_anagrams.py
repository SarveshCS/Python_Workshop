str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

def checkAnagram(str1, str2):
    hmap = {}
    if (ln:=len(str1)) != len(str2):
        return False
    for i in range(ln):
        if str1[i] in hmap:
            hmap[str1[i]] += 1
        else:
            hmap[str1[i]] = 1
            
        if str2[i] in hmap:
            hmap[str2[i]] -= 1
        else:
            hmap[str2[i]] = 1

    for i in hmap:
        if hmap[i] != 0:
            return False
    return True

if checkAnagram(str1.lower(), str2.lower()):
    print('yes they are anagrams')
else:
    print('No they are not anagrams')