def isimAl(*args,**kwargs):
    toplam = 0
    for i in args:
        toplam +=i
    for i in kwargs.items():
        print(i)
    return "toplam = {} ,key sayisi ={}".format(toplam,len(kwargs.items()))  

a = isimAl(1,2,3,4,5,mert="sis",tolgahan = "cayliyak",betul = "yildirim",ilayda ="boz") 
print(a)    
"""
def toplama(*arguman):
    for i in arguman:
        print(i)
        

toplama(1,2,3,4,5,6,7,8,9,10)

def toplama(**arguman):
    print(arguman)
    for i in arguman.items():
        print(i)
    for i in arguman.keys():
        print(i)

toplama(Istanbul = "10000000", Bursa = "2000000", Karabuk="250000")
"""

#degiskenlerin sayisi bilinemiyorsa kullanıyor :)