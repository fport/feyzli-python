import time as zaman
import random

class Winamp():
    def __init__(self,sarkilar=[]):
        self.sarkilar = sarkilar
        self.durum =True
        self.ses =100
        self.calanSarki =" "
    def sesArttir(self):
        if(self.ses >= 96):
            pass
        else:
            print("Ses Arttiriliyor...")
            zaman.sleep(2)
            self.ses += 5
            print("Ses Arttirildi... Güncel Ses : {}".format(self.ses))

    def sesAzalt(self):
        if(self.ses <= 0):
            pass
        else:
            print("Ses Azaltiliyor...")
            zaman.sleep(2)
            self.ses -= 5
            print("Ses Azaltildi...Guncel Ses : {}".format(self.ses))
    #sarki eklemeye yarar
    def sarkiEk(self,sarki):
        self.sarkilar.append(sarki)

    #Sarki listesini ekrana gösterir
    def sarkiListesi(self):
        print(self.sarkilar)

    #Sarki secmeye yarar
    def sarkiSec(self):
        sayac = 1
        for i in self.sarkilar:
            print("{}. {}".format(sayac,i))
            sayac+=1
        secim = int(input("Sarki numarasini giriniz"))
        print("Sarki degistiriliyor...")
        zaman.sleep(2)
        self.calanSarki = self.sarkilar[secim-1]
        print("Sarki degistirildi,Suan calan sarki = {}".format(self.calanSarki))
    #random sarkı acsın
    def rastgeleSarki(self):
        rastgele_sayi = rastgele.randint(0,len(self.sarkilar))
        self.calanSarki = self.sarkilar[rastgele_sayi]
    def kapa(self):
        self.durum = False
    def sarkiSil(self):
         secim = int(input("Silmek istediginiz sarkinin numarasini giriniz"))
         self.sarkilar.pop(secim-1)
    def arayuz(self):
       print("""
        Sarki Listesi = {}
        Suan Calan Sarki = {}
        Ses = {}
        Durum = {}
        
        1 - Sarki Sec
        2 - Ses Arttir
        3 - Ses Azalt
        4 - Rasgele Sarki Sec
        5 - Sarki Ekle
        6 - Sarki Sil
        7 - Sarki Kapa
        
        """.format(self.sarkilar,self.calanSarki,self.ses,self.durum))

o1 = Winamp(sarkilar=["Ahmet Kaya - Oy Benim Canim"])

while True:
    o1.arayuz()
    secim = int(input("Seciminizi girebilirsiniz :"))
    if(secim == 1):
        o1.sarkiSec()
    elif(secim == 2):
        o1.sesArttir()
    elif(secim == 3):
        o1.sesAzalt()
    elif(secim == 4):
        o1.rastgeleSarki()
    elif(secim == 5):
        sarki = input("Sarki Giriniz")
        o1.sarkiEk(sarki)
    elif(secim == 6):
        o1.sarkiSil()
    else:
        o1.kapa()