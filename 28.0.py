#ufak tefek orn
#Bir sayinin tam sayi bölenleri

def tamSayiBölenleri(sayi):
    liste = list()
    for i in range(1,sayi+1):
        if sayi % i ==0:
            liste.append(i)
    return liste


#print(tamSayiBölenleri(10))

#Bir sayinin asal olup olmadıgını
def asalMı (sayi):
    liste = list()
    for i in range(2,sayi):
        if sayi%i == 0:
            return False
    return True


print(asalMı(5))