class isci():
    def __init__(self,maas,isim,yasi):
        self.maas = maas
        self.isim = isim
        self.yasi = yasi

    def bilgileriGöster(self):
        print("""
        İsim : {}
        Yas : {}
        Maas :{}
        """.format(self.isim,self.yasi,self.maas))

class Yonetici(isci):

    def __init__(self,maas,isim,yasi,yetkinlik):
        super().__init__(maas,isim,yasi)
        self.yetkinlik = yetkinlik
     def  maasGuncelle(self,maas):
        self.maas = maas
     def bilgileriGöster(self):
        print("""
        İsim : {} Bey
        Yas : {}
        Maas :{}
        Yetkinlik :{}
        """.format(self.isim,self.yasi,self.maas,self.yetkinlik))
"""
isci1 = isci(2000,"Furkan",25)
isci1.bilgileriGöster()

y1 = Yonetici(5000,"Porti",32)
y1.bilgileriGöster()

y1 = Yonetici()
y1.bilgileriGöster()"""

y1 = Yonetici(10000,"ali",40,True)
y1.bilgileriGöster()
