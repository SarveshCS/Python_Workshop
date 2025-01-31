a = input('Enter a:')
b = input('Enter b:')

try:
    print('Answer:', int(a)/int(b))
except ZeroDivisionError:
    print('Second values \'b\' can not be Zero')
except ValueError:
    print('Second values \'b\' can not be a non integer')
finally:
    print('The programs was executed')