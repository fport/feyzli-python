def kareAl(liste):
    yeniliste = list()
    for i in liste:
        yeniliste.append(i**2)
    return yeniliste

print(kareAl([1,2,3,4,5,6,7,8,9,10]))


def kare(x):
    return x**2

print(list(map(kare,[1,2,3,4,5,6,7,8,9,10])))

a = list(map(lambda x : x**2,[1,2,3,4,5,6]))
print(a)