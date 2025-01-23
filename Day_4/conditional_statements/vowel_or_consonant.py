a = input('Enter char: ')


if a.lower() in 'aeiou':
    print('Vowel')
elif a.lower()>='a' and a.lower()<='z':
    print('Consonent')