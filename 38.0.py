"""
PortiCode

"""

class Ulke():
    def __init__(self,ulkeIsmi,nufus):
        self.ulkeIsmi = ulkeIsmi
        self.nufus = nufus

    def ulkeKurucu(self):
        return "Mustafa Kemal ATATURK"

    def __str__(self):
        return "Ulke : {} Nufus : {}".format(self.ulkeIsmi,self.nufus)

    def __len__(self):
        return self.nufus

turkiye = Ulke("Türkiye",810000000)
print(turkiye)
print(len(turkiye))

turkiye.ulkeKurucu()
# del turkiye

print(turkiye.ulkeKurucu())

