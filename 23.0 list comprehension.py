#List Comprehension

"""liste = [1,2,3,4,5,6]
liste2 = list()

for i in liste:
    liste2 =[i for i in liste]
    #liste2.append(i)
print(liste2)"""
"""
liste = []

for i in range(0,101):
    if i % 2 == 0:
        liste.append(i)

print(liste)

liste = [i for i in range(0,101) if i % 2 == 0 and i % 3 ==0]
print(liste)""""""
liste1 = [(1,2),(3,4),(5,6),(7,8)]
liste2 = [i*j for i,j in liste1]
print(liste2)

yazi = "Mert"
print(type(yazi))
liste = list(yazi)
print(liste)


yazi = "Porti"

liste = [harf*3 for harf in yazi]
print(liste)"""
"""
liste = [[1,2,3],[7,8,9],[10,20,30]]
#list comprehension ile kısa hali :/
liste2 = [ x for i in liste  for "x" in i]
print(liste2)
"""
#-----------------------------------------#
"""
for i in liste:
    for j in i:    #uzun yolu
        print(j)"""

#-----------------------------------------#
liste = [x**2 for x in range(0,11)]
print(liste)
