""" def selamVer(isim):
    print(isim)
    
fobjesi = selamVer

# >> print(type(fobjesi)) >> <class 'function'>
 
# >> fobjesi("Mehmet")

"""
def toplama(neKadar):
    def islemYap():
        toplam = 0    
        for i in range(0,neKadar+1):
            toplam+=i
        return toplam
    
    print("Bakin ben calistim !")
    
    print(islemYap())
    
#toplama(20)
    
fobjesi = toplama

fobjesi(10)