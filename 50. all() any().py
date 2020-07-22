def degerDondur(x):
    for i in x:
        if not i:
            return False
    return True


liste =  [True,True,True,True,True]
listex = [False,True,True,True,True]

print(degerDondur(liste))
print(degerDondur(listex ))

#KISA YOL#

liste = [False,True,True,True,True]

print(all(liste))
liste = [True,True,True,True,True]
print(all(liste))
liste = [False,False,False,False,False]
print(all(liste))
