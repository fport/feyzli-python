#PortiCode

def toplamAl(liste):
    if type(liste) == list or type(liste) == tuple:
        toplam = 0
        for i in liste:
            toplam +=i
        return toplam
    else:
        raise ValueError("Girilen parametre liste veya tuple bekleniyordu")
"""
a = toplamAl([1,2,3,4,5,6])
b = toplamAl((1,2,3,4,5,6))
c = toplamAl("Porti")
print(c)# Hata alcak!
print(b)
print(a)
"""

try :
    a = toplamAl(5)
    print(a)
except ValueError:
    print("Buraya girdi")