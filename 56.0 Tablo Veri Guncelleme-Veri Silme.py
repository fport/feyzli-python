import sqlite3

baglanti = sqlite3.connect("market.db")
isaretci = baglanti.cursor()

def tablo_olustur():
    isaretci.execute("create table if not exists Urunler(urunAd TEXT,marka TEXT,fiyat INT,adet INT)")
    baglanti.commit()
def tablo_veri_ekle(urunad,marka,fiyat,adet):
    isaretci.execute("insert into Urunler values(?,?,?,?)",(urunad,marka,fiyat,adet))
    baglanti.commit()
def tablo_veri_cek():
    isaretci.execute("select *from Urunler")
    veriler = isaretci.fetchall()
    for i in veriler:
        print(i)
        
def tablo_guncelle(eskiIsim,yeniIsim):
    isaretci.execute("update Urunler set urunad = ? where urunad = ?",(eskiIsim,yeniIsim))
    baglanti.commit()

def tablo_veri_sil(urunad):
    isaretci.execute("Delete from Urunler where urunad = ?",(urunad,))
    baglanti.commit
        
tablo_olustur()
tablo_veri_sil("Sufle")
tablo_veri_cek()