"""
c = 10

def carp(a,b):
    c=5
    print(c)
    return a*b

print(c)

print(carp(1,3))"""
c = 10
"""
def carp(a,b):
    global c
    return a*b*c

print(carp(1,3))"""
#Lamda Fonksiyonu
#tek satırda fonk yazma
"""
def kuvvetal(taban,kuvvet):
    return taban*kuvvet
 print(kuvvetAl)
"""
kuvvetAl = lambda taban,kuvvet : taban**kuvvet
print(kuvvetAl(2,5))

tek_cift = lambda x : x % 2== 0

deger = int(input("Sayi giiir:"))

if tek_cift(deger):
    print("Cift sayidir")
else:
    print("Tek Sayidir.")
