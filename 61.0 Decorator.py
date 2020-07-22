           """
>> Decorator Fonksiyonlar <<

           """

import time

def zamanBul(fonksiyon):
    def wrapper(sayilar):
        zaman = time.time()
        islem = fonksiyon(sayilar)
        yeni_zaman = time.time() - zaman
        print("{} fonksiyonu bu kadar zaman surdu : {}".format(fonksiyon.__name__,yeni_zaman))
        return islem
    return wrapper

@zamanBul
def faktoriyelAl(faktoriyelSayisi):
   # zaman = time.time()    
    faktoriyel = 1
    for i in range(1,faktoriyelSayisi+1):
        faktoriyel = faktoriyel * i
    #sonuc = "bu fonksiyon su kadar zamanda olustu : {}, faktoriyel = {}".format(time.time()-zaman,faktoriyel)
    #print(sonuc)
    return faktoriyel
@zamanBul
def kareleriAl(sayilar):
    #zaman = time.time()
    liste = list()
    for i in sayilar:
        liste.append(i**2)
    #sonuc = "Gecen zaman = {}, yeni liste = {}".format(time.time()-zaman,liste)
    #print(sonuc)
    return liste
"""   
faktoriyelAl(5)
kareleriAl(range(100000))
"""
faktoriyelAl(1000)
kareleriAl(range(100000))

