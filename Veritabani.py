
import sqlite3

baglanti = sqlite3.connect("ogrenciler.db")
isaretci = baglanti.cursor()
def tablo_olustur():
    
    isaretci.execute("create table if not exists ogrenciler(isim TEXT,soyad TEXT,Dogum_tarihi INT)")
    baglanti.commit()#veritabanini güncelledik
   
def tablo_veri_ekle(isim,soyad,dogum_tarihi):
    #isaretci.execute("insert into ogrenciler values('{}','{}',{})".format(isim,soyad,dogum_tarihi))
    isaretci.execute("insert into ogrenciler values(?,?,?)",(isim,soyad,dogum_tarihi))
    baglanti.commit()
    
    
    
tablo_olustur()
isim = input("İsim giriniz : ")
soyad = input("Soyisim giriniz :")
dogum_tarihi = int(input("Dogum tarihi giriniz :"))
tablo_veri_ekle(isim,soyad,dogum_tarihi)

baglanti.close()

