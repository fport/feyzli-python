#  findALL()

import re

metin = """
Lorem ipsum dolor python sit amet, consectetur 
adipiscing elit. In mollis erat id justo efficitur 
dignissim. Vivamus justo enim, tincidunt sit amet auctor
 eu, convallis vel erat.python Donec nulla ligula, lacinia vel
 sapien vitae, varius tincidunt dolor. Mauris at malesuada
 justo. Donec posuere erat eu python erat condimentum rhoncus.
 Suspendisse potenti. Duis semper lacus in faucibus
 rhoncus. Nunc ut feugiat mauris. python
 Morbi rhoncus lacinia nunc, vel semper orci blandit non.

"""

a = re.findall("python",metin)
print(a)

liste = list()
for i in metin.split():
    nesne = re.search("python",i)
    
    if nesne : 
        liste.append(nesne.group())
print(liste)