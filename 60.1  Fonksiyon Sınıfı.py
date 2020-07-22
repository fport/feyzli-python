"""def isimBagir(isim):
    print("{}!!!".format(isim))
    
isimBagir("Porti")

a = "Ali"

print(type(a))
"""

def toplama(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam

def faktoriyelAl(faktoriyelSayisi):
    faktoriyel = 1
    for i in range(1,faktoriyelSayisi+1):
        faktoriyel=faktoriyel*i
    return faktoriyel

def islemYap(fonk1,fonk2,islem):
    if islem == "toplama":
        sayac = 1
        liste = list()
        while True:
            try:
                sayi = int(input("{}.ci sayiyi giriniz : (yeterli kadar  sayi girdinizi dusunuyosaniz 'q' giriniz )".format(sayac)))
                liste.append(sayi)
                sayac += 1
            except ValueError:
                break
        print(fonk1(liste)) 
    else:
        faktoriyel = int(input("Kac faktoriyel =>>"))
        print(fonk2(faktoriyel))
        
        
islemYap(toplama,faktoriyelAl,"j")