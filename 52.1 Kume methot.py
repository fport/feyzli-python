#PortiCode - Kumeler

kume1 = {1,2,3,4,5,6,6,6,7,8,9}
kume2 = {-20,15,1,25,49,6,7}
"""
print(kume1.difference(kume2))
print(kume2.difference_update(kume1))
print(kume1)

"""
"""
kume2.add(50)
print(kume2)
"""

kume1.discard(5)
print(kume1.intersection(kume2))
print(kume1.isdisjoint(kume2))#Ayrık kümemi

kum1 = {1,2,3,4}
kum2 = {1,2}
print(kum2.issubset(kum1))#Alt küme


kum1 = {1,2,3,4}
kum2 = {1,2,5,7}

print(kum2.union(kum1))