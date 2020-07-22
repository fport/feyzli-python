"""
PortiCode

"""
#EBOB = 30 15 = ebob(30,15) = 15
#EKOK = 30 20 = ekok(30,20) = 60

def ebob(a,b):
    kucuksayi = min(a,b)
    ortak_bolenler = list()
    for i in range(1,kucuksayi+1):
        if a % i == 0 and b % i == 0:
            ortak_bolenler.append(i)
    ortak_bolenler.sort(reverse=True)
    return ortak_bolenler[0]

def ekok(a,b):
    ortak_bolenler = list()
    for i in range(1,a*b):
        if i % a == 0 and i % b == 0:
            ortak_bolenler.append(i)
    ortak_bolenler.sort()
    return ortak_bolenler[0]

print(ebob(15,30))
print(ekok(40,20))