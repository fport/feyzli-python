a =  1 == 1 and 1<5# (&&) c deki
print(a)
a =  3 == 3 and 6<5
print(a)

b = 2 != 2 or "Porti" == "Porti"
print(b)

c= not 5<=5 or "Mert" == "Furkan"#not trueysa false yapar.
print(c)

sayi = int(input("Bir sayi giriniz : "))

a = sayi % 2 == 0
b = sayi % 2 == 1

print("Cift'in dogruluk degeri = {} \n Tek'in dogruluk degeri = {} ".format(a,b))
