import sqlite3

baglanti = sqlite3.connect("sirket.db")
imlec = baglanti.cursor()

def tablo_olustur():
    imlec.execute("create table if not exists calisanlar(isim TEXT,soyad TEXT,pozisyon TEXT,maas INT)")
    baglanti.commit()
    
def tabloVeriEkle(isim,soyisim,pozisyon,maas):
    imlec.execute("insert into calisanlar values (?,?,?,?)",(isim,soyisim,pozisyon,maas))
    baglanti.commit()
"""    
def tabloVeriCek():
    imlec.execute("select * from calisanlar")
   # imlec.execute("select isim,maas from  calisanlar")
   veriler = imlec.fetchall()
    print(veriler)
    for i in veriler:
        print(i)
"""

def tabloVeriCek(pozisyon):
    imlec.execute("select * from calisanlar where pozisyon = ?",(pozisyon,))#virgül koymassan tuple olarak algılamıyor 
    veriler = imlec.fetchall()
    print(veriler)
    for i in veriler:
        print(i)



        
tablo_olustur()
while True:
    veri = input("Veri Eklemek icin 1, cikmak icin 'q'ya basiniz")
    if veri == 'q':
        break
    isim = input("İsim giriniz :")
    soyad = input("Soyad giriniz :")
    pozisyon = input("Pozisyon giriniz")
    maas = int(input("Maas giriniz"))
    
    tabloVeriEkle(isim,soyad,pozisyon,maas)

almakIstenilen = input("Almak istediginiz pozisyonu giriniz :")

tabloVeriCek(almakIstenilen)
    
