import time as zaman
import sqlite3

class Ogrenci():
    
    def __init__(self):
        self.baglanti = sqlite3.connect("ogrencile.db")
        self.isaretci = self.baglanti.cursor()
        self.tablo_olustur()
        
    def tablo_olustur(self):
        self.isaretci.execute("create table if not exists ogrencile(kisi TEXT,harfnotu TEXT,durum TEXT)")
        self.baglanti.commit()
    
    def tablo_veri_ekle(self,kisi,harfnotu,durum):
        self.isaretci.execute("insert into ogrencile Values(?,?,?)",(kisi,harfnotu,durum))
        self.baglanti.commit()
        
    def tablo_veri_cek(self):
        self.isaretci.execute("select *from ogrencile")
        veri = self.isaretci.fetchall()
        for i in veri:
            print(i)
        self.baglanti.commit()
    
    def tablo_veri_guncelle(self,isim,yeniIsim):
        self.isaretci.execute("update ogrencile set = ? where = ?",(yeniIsım,isim))
        self.baglanti.commit()
    
    def tablo_veri_sil(self,isim):
        self.isaretci.execute("delete from ogrencile where = ?",(isim))
        self.baglanti.commit()
        
    def notHesapla(self,vize,final):
        durum = (vize*0.4)+ (final*0.6)
        return durum
        self.baglanti.commit()
    
    def basariDurum(self,durum):
        if durum > 90:
            return "AA"
        elif durum > 85:
            return "BA"
        elif durum > 80:
            return "BB"
        elif durum > 75:
            return "CB"
        elif durum > 70:
            return "CC"
        elif durum > 65:
            return "DC"
        elif durum > 60:
            return "DD"
        else:
            return "FF"
        self.baglanti.commit()
ogrenci = Ogrenci()

while True:
    secim = input("""
    *********************Bursa Teknik Universitesi*********************
    *********************Veri Tabanina Hosgeldiniz*********************
    
    >> Veri Eklemek icin herhangi bir tusa basin, cikmak icin 'q' basiniz
    
    """)
    if secim == 'q':
        break
    
    isim = input(">> Ogrencinin adini ve soyadini giriniz :")
    vize = float(input(">> Ogrencinin vize notunu giriniz :"))
    final = float(input(">> Ogrencinin final notunu giriniz :"))
    
    print("Hesaplaniyor")
    for i in range(3):
        zaman.sleep(1)
        print(".",end ="")
    print("Basariyla veri tabanina eklendi !")
    
    durum = ogrenci.notHesapla(vize,final)
    harf_notu = ogrenci.basariDurum(durum)
    if durum > 60:
        ogrenci.tablo_veri_ekle(isim,harf_notu,"Basarili")
    else:
        ogrenci.tablo_veri_ekle(isim,harf_notu,"Basarisiz")
        
    print("\n Güncel Veri Tabani :")
    ogrenci.tablo_veri_cek()
