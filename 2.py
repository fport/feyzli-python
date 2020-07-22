#dairenin alani
"""
a = 5
b = 10

a,b = b,a
print(a)
print(b)

a=5
a= a+1 #a+=1 aynı sey
print(a)

#paramatresine göre girilen sayinin tek veya cift olup olmadıgını bool olarak dondurur
"""
def tekmi(sayi):
    if(sayi%2 == 0):
       return print("Sayi çiftir...")
    else:
        return print("Sayi tektir...")

tekmi(5)
