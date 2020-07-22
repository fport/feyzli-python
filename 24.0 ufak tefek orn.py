import time as zaman
"""

PortiCode

"""

#Ornek
print("BlaBla Bank Hosgeldiniz!\tIslem Yapmak Icın Kartınızı Sokunuz!")
secim = input("Kartı Sokmak icin s,Bankamatıkten Ayrılmak icin l yazınız")

mevcutpara=1000

if(secim =='s'):
    print("Kartiniz okunuyor", end="")
    for i in range(3):
        print(".",end = "")
        zaman.sleep(1)
    while True:
        secenek = int(input("""
        ************************
        1-KARTA PARA YUKLE
        2-KARTTAN PARA CEK
        3-HESAP OZETİ 
        4-CIKIS
        ************************
        """))
        while secenek < 1 or secenek > 4:
            secenek = int(input("Lutfen 1-4 arası bir secenek giriniz!!!"))
        if secenek ==1:
            miktar = int(input("Miktar Giriniz"))
            mevcutpara+=miktar
            for i in range(3):
                print(".", end="")
                zaman.sleep(1)
        elif secenek ==2:
            miktar = int(input("Miktari Giriniz"))
            mevcutpara-=miktar
            for i in range(3):
                print(".", end="")
                zaman.sleep(1)
        elif secenek == 3:
            print("""
            ********************
            ISIM : Furkan   
            SOYISIM : Portakal
            IBAN : XXXXXX
            BAKIYE : {}
            """.format(mevcutpara))
        elif secenek == 4:
            break
