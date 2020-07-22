"""def fonksiyon(belirle):
    try:
        liste = [x for x in range(100) if x % belirle ==0]
        print(liste)
    except TypeError:
        print("Fonksiyona Gönderilen deger hatali")

fonksiyon("mert")
"""
"""
def fonksiyon(p1,p2,p3):
    return p1+p2+p3
print(fonksiyon(1,2,3))"""
#arg yerine baska bişeydene koyabılırsın
def fonksiyon(*args):
    toplam =0
    for i in args:
        toplam+=i
    return print(toplam)


fonksiyon(1,2,3,4,5,6,7,8)

def yazdir(*kelime):
    for i in kelime:
        print(i,end=" ")

yazdir("yegen","sude")

def daireAlan(r,PI =3.1415):
    return print(PI*(r**2))

daireAlan(5)# piyi kendi alıyor
daireAlan(5,3)#piyi biz degiştiriyoruz
daireAlan(5, PI=3)

