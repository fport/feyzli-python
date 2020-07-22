import re

liste = ["özcan","esma","özlem","mehmet","selim",
       "süleyman","esin","dündar","esra","özkan","özhan"]


for isim in liste:
    nesne = re.search("öz[kch]an",isim)
    
    if nesne:
        print(nesne.group())

for isim in liste:
    nesne = re.search("es[mr]a",isim) 
    
    if nesne:
        print(nesne.group())
