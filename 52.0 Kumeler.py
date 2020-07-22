#PortiCode - Kümeler

kume1 = {1,2,3,4,5,6,6,6}
kume2 = {10,20,30,2,3,4,5}
liste =[1,2,3,4,5,6,5,5,6]

kume3 = set(liste)
print(kume3)#Kume yapılarında her birinden 1 tane bulunur

yazi = "Java nesne tabanli bir programlama dilidir"

kume = set(yazi)
print(kume)

yazilimDilleri = ["Php","Javascript","Python","Php"]
kume=set(yazilimDilleri)
print(kume)
for i in yazilimDilleri:
    print(i,end=" ")

yazilimDilleri = {"Php","Javascript","Python","Php"}
#print(yazilimDilleri[0])#TypeError: 'set' object is not subscriptable

