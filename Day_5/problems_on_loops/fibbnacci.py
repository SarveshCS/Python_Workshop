# n = int(input('Enter a number: '))
# a = 0
# b = 1
# c = 0
# i = 0
# while i < n:
#    print(a)
#    c = a+b
#    a = b
#    b = c
#    i+=1


n = int(input('Enter a number: '))
a = 0
b = 1
i = 0
while i < n:
   print(a)
   b = a+b
   a = b-a
   i+=1