import re

#match
#Bulunan karakter dizini (string )objemizin
# bastan itibaren icerigini tarar
"""
yazi = "Python güclüdür"
# >> print(re.match("Python",yazi))
reNesnesi = re.match("Python",yazi)

print(reNesnesi.span())

bas,son = reNesnesi.span()
print(yazi[bas:son])
"""

"""
yazi = input(">> Bir yazi giriniz <<\n")

yaziAl = re.match("Mert Sis",yazi)

if yaziAl:
    bas,son = yaziAl.span()
    print(yazi[bas:son],"bulunmakta")
else:
    print("boyle bir yazi yok !")
    
"""

yazi = "Porti Code youtube channel"

print(re.match("Code",yazi))
#icinde olmasına ragmen bastan ıtıbaren kontrol ettıgı ıcın 