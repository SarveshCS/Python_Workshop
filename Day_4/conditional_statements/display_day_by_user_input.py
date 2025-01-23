a = int(input('Enter the day number: '))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thrushday', 'Friday', 'Saturday']


try:
    if a<= 0:
        raise Exception
    print(days[a-1])
except:
    print('Wrong Input')