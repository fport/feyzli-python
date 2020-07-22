#Generator
"""
liste  = list()
for i in range(100):
    liste.append(i**2)
    
for i in liste:
    print(i)
"""
def sayilariKaresiniAl():
    for i in range(1,101):
        yield i**2 #cagırdigimiz zaman calıscak
        
iterator = iter(sayilariKaresiniAl())

print(next(iterator)) #1 yazdırcak ve hafızadan silcek
print(next(iterator)) # fazla bellek tutması gereken yerlerde generator kullanıyor.
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
        
        