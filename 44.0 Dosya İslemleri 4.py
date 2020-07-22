with open("takimlar.txt","r+") as dosya:
    try:
       icerik = dosya.read()
       icerik = "Trabzonspor\n" + icerik
       dosya.seek(0)
       dosya.write(icerik)

    except FileNotFoundError:
        print("Dosya bulunamadi")