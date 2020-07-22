import time
import random
import oyun

def sayiAl():
    sayi_tahmin = int(input("Sayiyi tahmin ediniz :"))
    return sayi_tahmin

def oyunBaslat():
    print("""
    
    >> Sayi Tahmin Oyununa Hosgeldiniz ! <<
    
    """)
    sayac = 0
    rasgele_sayi = random.randint(1,101)
    while True:
        sayitahmin = sayiAl()

        if(sayitahmin > rasgele_sayi):
            print("Kontrol Ediiyor",end="")
            for i in range(3):
                print(".",end ="",sep="")
                time.sleep(1)
            print("Girdiginiz sayi Rasgele Gizli sayidan buyuktur")
        elif(sayitahmin < rasgele_sayi):
            print("Kontrol Ediiyor", end="")
            for i in range(3):
                print(".", end="", sep="")
                time.sleep(1)
            print("Girdiginiz sayi Rasgele Gizli sayidan kucuktur")
        else:
            print("Kontrol Ediiyor", end="")
            for i in range(3):
                print(".", end="", sep="")
                time.sleep(1)
            print("Tahmininiz DOĞRU !!!")
        sayac +=1