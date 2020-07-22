def enumYapma(liste):
    bliste = list()
    for i in range(len(liste)):
        bliste.append((i,liste[i]))
    return bliste

print(enumYapma(["porty","port","forti","furki"]))

for i,j in enumYapma(["ALi","Veli","Ayse","Fatma","Hayriye"]):
    print("{}.index : {} isim var!".format(i,j))


print(list(enumerate(["İstanbul","İzmir","Bursa","Antalya","Adana","Ankara"])))
