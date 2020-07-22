# İteratorler
"""
liste = [1,2,3,4,5]

iterasyon = iter(liste)

for i in liste(i):
    print(i)
    
while True:
    try:
        print(next(iterasyon))
    except StopIteration:
        break

"""

class sarkilar():
    def __init__(self,liste):
        self.liste = liste
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.liste):
            return self.liste[self.index]
        else:
            self.index -=1
            raise StopIteration

sarkilar = sarkilar(["İtirazim var","Abba","Bir sonraki hayatimda gel","Lolo"])

iterasyon = iter(sarkilar)
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
