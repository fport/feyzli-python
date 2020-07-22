def top(a,b):
    return a+b

def cık(a,b):
    return a-b
def bol(a,b):
    return a//b
def carp(a,b):
    return a*b
def fak(a):
    fakt = 1
    for i in range(1,a+1):
        fakt *=i
    return fakt
def asal_mi(sayi):
    for i in range(2,sayi):
        if(sayi % i == 0):
            return false
        return True