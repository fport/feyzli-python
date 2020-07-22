"""liste = ["Ankara","İstanbul","Karabük"]
sozluk = {"Bir":1,"İki": 2}
demet = (1,2,3,4,5,6)

class Araba():
    renk = "Gri"
    silindir = 4
    model = "Peugeout"
    plaka = "78 BK 286"


araba1 = Araba()

print(araba1.model,araba1.plaka,araba1.renk)
print(dir(araba1))"""

class Araba():
    def __init__(self,renk="Rengi yok",silindir= 0,model=""):
        print("Nesne olusturuldu !")
        self.r = renk
        self.s = silindir
        self.m = model

print("Nesne Olusmustu")
araba1= Araba("MAvi",4,"Renault Clio")
print(araba1.m,araba1.r,araba1.s)

araba2 = Araba("Kirmizi",5,"Suzuki")
print(araba2.m,araba2.r,araba2.s)

araba3=Araba("Mavi")
print(araba3.r)