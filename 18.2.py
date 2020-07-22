#Hesap Makinasi

secim =int(input("1-Toplama\n2-Çıkarma\n3-Carpma\n4-Bolme\n5-Cikis\nYapmak istediginiz islemi (rakam) giriniz :"))

sonuc = None

if secim != 5:
    sayibir = float(input("Birinici sayiyi giriniz :"))
    sayiiki = float(input("İkinci sayiyi giriniz :"))
    if secim == 1:
        sonuc = sayibir + sayiiki
        print("{} + {} = {}".format(sayibir, sayiiki, sonuc))
    elif secim == 2:
        sonuc = sayibir - sayiiki
        print("{} - {} = {}".format(sayibir, sayiiki, sonuc))
    elif secim == 3:
        sonuc = sayibir * sayiiki
        print("{} * {} = {}".format(sayibir, sayiiki, sonuc))
    elif secim == 4:
        sonuc = sayibir / sayiiki
        print("{} / {} = {}".format(sayibir, sayiiki, sonuc))
else:
    pass


print("Program sonlandı...")