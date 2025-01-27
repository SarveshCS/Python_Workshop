def xyz(num):
    def pqr(n):
        return n+1
    result = pqr(num)
    return result
print(xyz(5))