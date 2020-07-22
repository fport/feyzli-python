a = "T.B.M.M 23 Nisan 1920'de kuruldu"
#print(a.upper())
#print(a.lower())
#print(a.replace(".","-")) #karakterleri degistir
#print(a.startswith("T.B"))
#print(a.startswith("T.A"))
#print(a.endswith("uldo"))
#print(a.split(" "))
"""
b = input("Virgullere ayirarak sevdiginiz 3 sanatciyi giriniz : (Bknz : Muslum Gurses, Zeki Muren, Muazzez Abaci)>>")

liste = b.split(",")
print(liste)
"""
"""
nickname = "XXXXXXPORTİXXXXXX"
print(nickname.lstrip("X"))
print(nickname.rstrip("X "))
print(nickname.strip("X"))
"""
liste = ["Fenerbahce","1907'te kuruldu","Renkleri Sari-Lavicert"]
print(liste)
print(" ".join(liste))

deneme = ["Turkiyenin en büyük lideri Recep Tayyip Erdogandır"]
print(a.count("a"))
print(a.find("i"))