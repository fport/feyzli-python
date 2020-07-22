"""
# demet Tuple

demet = (1,2,3,4,5)
print(demet)
print(type(demet ))
#demet[2]=bla bla diye atama yapamazsın
yenidemet = demet[::2]
print(yenidemet)

yazi = "Porti Code"
demet = tuple(yazi)
print(demet)
"""

demet = (1,2,3,4,5,5,"Porti",6,7,8)
print(demet.index(1))#diyorkiii 1 kaçıncı indexte
print(demet.index("Porti"))
isim=demet[6]
print(isim)

saydır=(1,1,1,1,2,2,2,3,3,3,3,3,4,5,4,6)
print(saydır.count(2))