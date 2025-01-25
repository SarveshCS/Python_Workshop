n = int(input('Enter a number:'))

def checkArmstrong(n):
    digits = 0
    t = n
    while t>0:
        t//=10
        digits+=1
    t = n
    su = 0
    while t>0:
        su += (t%10) ** digits
        t//=10
    return su == n

if checkArmstrong(n):
    print('Armstrong')
else:
    print('Not armstrong')