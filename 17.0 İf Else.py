# if else blokları

a= int(input("a degerini giriniz"))
b= int(input("b degerini giriniz"))

if a>b:
    print("{} > {}".format(a,b))
elif a<b:
    print("{} < {} ".format(a,b))
elif a==b:
    print("{} = {} ".format(a, b))
    

girilensayi = int(input("bir tam sayi giriniz : "))

if (girilensayi % 2) == 0:
    print("Sayimiz cifttir")
else:
    print("Sayimiz tektir ")