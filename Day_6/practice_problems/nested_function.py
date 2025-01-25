a = 10
def XYZ():
    global a
    print('a1:', a)
    a = 20
    print('a2:', a)
    def PQR():
        print('a3:', a)
        a = 30
        print('a4:', a)
    PQR()
XYZ()