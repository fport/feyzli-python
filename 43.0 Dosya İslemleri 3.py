try:
    with open("takimlar.txt","r") as dosya:
        a=dosya.read()
        print(a)
        print(len(a))
        print(dosya.tell())#imlecin nerde oldugunu soyler
        dosya.seek(5)#imleci istedigin byte getirme
        print(dosya.tell())
except FileNotFoundError:
    print("Boyle bir dosya bulunamadi !")
