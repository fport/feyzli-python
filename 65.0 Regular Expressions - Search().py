import re

# <<search>>
# metinsel ifadelerimizin icinde gezinti
# yaparak istedigimiz yazinin bas ve 
# son degerlerini elde ederiz ve varsa 
# Nesbe elde ederiz

yazi = """
Python 3.7.4 (default, Aug  9 2019, 
 18:34:13) [MSC v.1915 64 bit (AMD64)]
Type "copyright", "credits" or "license"
 for more information.

"""

eslesme = re.search("Python",yazi)
# print(eslesme.group())#eslestigi degeri donduruyor
# print(eslesme.span())
"""
liste = ["kebap","lahmacun","iclikofte"]

eslesme = re.search("lahmacun",liste)

>>typeeror expected string or bytes-like object
<< alttaki gibi düzeltebiliriz
"""
"""
liste = ["şiş kebap","kebap","lahmacun","iclikofte"]

for i in liste:
    reobje = re.search("kebap",i)
    print(reobje)
"""
liste = ["şiş kebap","kebap","lahmacun","iclikofte"]

for i in liste:
    reObje = re.search("kebap",i)
    if reObje:
        print(reObje.group())
    else:
        print("Kebap bulunmamaktadir")
    
    
    