import sqlite3

def tablo_olustur():
    baglanti = sqlite3.connect("ogrenciler.db")
    isaretci = baglanti.cursor()
    isaretci.execute("create table if not exists ogrenciler(isim TEXT,soyad TEXT,Dogum_Tarihi INT)")
    baglanti.commit()
    baglanti.close()


tablo_olustur()


