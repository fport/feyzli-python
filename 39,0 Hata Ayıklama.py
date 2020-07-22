#PortiCode

while True:
    try:
        kontrol = input("Çıkmak icinn 'q'basiniz...Devam icin herhangi bir sey :")
        if kontrol == 'q':
            break
        sayi1 = int(input("Birinci sayiyi giriniz :"))
        sayi2 = int(input("İkinci sayiyi giriniz"))
        print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))
    except ValueError:
        print("Girdiginiz sayi tam sayi degildir!")


try:
expect: yazıp bırakırsak 28 hatada da aynı print yazdirabiliriz
finally: ben hertürlü calısırım
