import random
"""
print("{}\n{}\n{}\n".format(random.random(),random.random(),random.random()))
"""
"""
print(random.uniform(0.5,2.5)) <--
print(random.randint(1,100)) <--

liste = ["Porti","Mert","Ergul","A","B"]
print(random.choice(liste)) <---
"""
"""
liste = [i for i in range(1,100) if i %3 == 0 ]
print(random.choice(liste))
"""
"""
birincir = ["b" + str(i) for i in range(1,14)]
ikincir = ["i" + str(i) for i in range(1,14)]
ucuncur = ["u" + str(i) for i in range(1,14)]
dorduncur = ["d" + str(i) for i in range(1,14)]

tum_taslar = [birincir,ikincir,ucuncur,dorduncur]

print(tum_taslar)

print(">>"+random.choice(tum_taslar[random.randint(0,3)]))
"""
"""
liste = [1,2,3,4,5,6,7,8,9]

random.shuffle(liste) <--
print(liste) # pass by referance style 
"""
"""

liste = [1,2,3,4,5,6,7,8,9]

print(random.sample(liste,3))

"""
"""
<< Tekrar >>

random.random() --> 0 ile 1 arasi random sayi donduruyor

random.uniform(1,100) --> belirtilen aralikta bir deger donduruyo

random.randint(1,100) -->     "         "       integer   "  

random.choise() --> verilen listeden  deger seciyo

random.shuffle() --> liste yer degistiriyo pass by referance yontemiyle

random.sample  --> random.sample(liste,3) 



