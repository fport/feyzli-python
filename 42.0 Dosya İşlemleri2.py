"""try:
    dosya = open("bilgiler.txt","r")

    for i in dosya:
        print(i)

    dosya.close()

except FileNotFoundError:
    print("Boyle bir dosya dizinde bulunmamaktarir!")
"""
"""
try:
    dosya = open("bilgiler.txt","r")


    icerik = dosya.read()
    print(icerik)
    icerik2 = dosya.read()
    print(icerik2)# bişey yazdırmıcak cunku .read imleci textin sonuna getirir
    dosya.close()
    #print(dosya.readline()) 1 satir okuyor


except FileNotFoundError:
    print("Boyle bir dosya dizinde bulunmamaktarir!")
"""
"""
try:
    dosya = open("bilgiler.txt","r")

    print(dosya.readline(),end = "")
    print(dosya.readline(),end = "")
    print(dosya.readline(),end = "" )

    dosya.close()

except FileNotFoundError:
    print("Boyle bir dosya dizinde bulunmamaktar")"""

try:
    dosya = open("bilgiler.txt","r")

    liste = dosya.readlines()
    print(liste)
    for i in liste:
        print(i)

    dosya.close()

except FileNotFoundError:
    print("Boyle bir dosya dizinde bulunmamaktar")