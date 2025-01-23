lst1 = list(range(1, 5)) if (lst:=input('Enter list 1: ')) == "" else lst.split()
lst2 = list(range(3, 26, 3)) if (lst:=input('Enter list 2: ')) == "" else lst.split()

while True:
    eq = input("$ ")
    eval(eq)