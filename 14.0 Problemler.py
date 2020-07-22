"""a = int(input("Dik kenar gir"))
b = int(input("Dik kenar gir"))
c = (a**2 + b**2)**0.5
print("Hipotenus :", c)

v = float(input("V gir"))
R = float(input("R gir"))

I = v//R
print("Akım :",I)"""


sozluk = dict()

while True:
    urun_ismi = input("Urun ismi giriniz =")
    if (urun_ismi == 'q'):
        break
    urun_adedi = input("Urun adedini giriniz")
    sozluk[urun_ismi] = urun_adedi


print(sozluk)
