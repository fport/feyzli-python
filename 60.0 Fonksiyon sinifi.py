def islem(islemAdi):
    
    def toplama(*sayilar):
        toplam = 0
        for i in sayilar:
            toplam += i
        return toplam
    
    def carpma(*sayilar):
        carpim = 1
        for i in sayilar:
            carpim*=i
        return carpim
    
    def faktoriyelAl(faktoriyelsayi):
        faktoriyel = 1
        for i in range(1,faktoriyelsayi+1):
            faktoriyel*=i
        return faktoriyel
    
    if islemAdi == "+":
        return toplama
    elif islemAdi == "*":
        return carpma
    else:
        return faktoriyelAl
    
toplam = islem("+")
print(type(toplam))
print(toplam(1,2,3,4,5))


carpim = islem("*")
print(carpim(1,2,3,4,5))

fak = islem("!")
print(fak(6))
