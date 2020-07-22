with open("takimlar.txt","r+") as dosya:
    liste = dosya.readlines()
    liste.insert(2,"Denizlispor\n")
    dosya.seek(0)
    for i in liste:
        dosya.write(i)