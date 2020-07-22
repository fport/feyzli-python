liste = [1,50,44,15,32]

print(max(liste))
print(min(liste))
print(max(15,11))

isci = ["Ahmet","Berna","Furkan","Sude"]
maas = [5700,5900,4500,5800]
print(list(zip(isci,maas)) )

def eslestir(liste1,liste2):
    liste = list()
    for i in range(len(liste1)):
        liste.append((liste1[i],liste2[i]))
    return liste

takimlar = ["GS","FB","BJK","TS"]
samp_sayisi = [21,28,16,7]

print(eslestir(takimlar,samp_sayisi))