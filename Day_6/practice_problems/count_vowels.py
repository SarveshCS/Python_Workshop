string = input('Enter string 1: ')

def countVowels(string):
    hmap = {}
    ln = len(string)
    for i in range(ln):
        if string[i] not in 'aeiou':
            continue
        if string[i] in hmap:
            hmap[string[i]] += 1
        else:
            hmap[string[i]] = 1
            
    return hmap

count = countVowels(string.lower())
for i in count:
    print(f"{i}: {count[i]}")