class Sirket():
    def __init__(self,calisansayisi,sirketismi,mudurler,muduryrd,faaliyet):
        self.calısansayisi = calisansayisi
        self.sirketismi = sirketismi
        self.mudurler = mudurler
        self.muduryrd = muduryrd
        self.faaaliyet = faaliyet

    def calısanAl(self,sayi):
        self.calısansayisi += sayi
    def calısanKov(self,sayi):
        self.calısansayisi -= sayi
    def sirketIsmiDegistir(self,isim):
        self.sirketismi = isim
    def sirketiBatir(self):
        self.faaaliyet = False
    def mudurEkle(self,isim):
        self.mudurler.append(isim)
    def muduryrd(self,isim):
        self.muduryrd.append(isim)
    def bilgileriGoster(self):
        print("""
        Sirket İsmi : {}
        Calisan sayisi : {}
        Mudurler : {}
        Mudur Yardimcilari : {}
        Sirket Aktif mi ? : {}
        """.format(self.sirketismi,self.calısansayisi,self.mudurler,self.muduryrd,self.faaaliyet))


PortiCode = Sirket(78,"PortiCode",["Furkan Portakal","Mert Sis"],["Mehmet Ekici","Ozan Tufan"],True)
PortiCode.calısanAl(10)
PortiCode.mudurEkle("Ali Koc")
PortiCode.sirketiBatir()
PortiCode.bilgileriGoster()

