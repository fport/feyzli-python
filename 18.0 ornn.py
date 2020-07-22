vize = float(input("Vize notunuz :"))
final = float(input("Final notunuz :"))
ortalama = vize*0.4 + final*0.6

if (ortalama >=90):
    print("Harf Notunuz : AA")
elif (ortalama >= 85):
    print("Harf Notunuz : BA")
elif (ortalama >= 80):
    print("Harf Notunuz : BB")
elif (ortalama >= 75):
    print("Harf Notunuz : CB")
elif (ortalama >= 70):
    print("Harf Notunuz : CC")
elif (ortalama >= 55):
    print("Harf Notunuz : CD")
elif (ortalama >= 50):
    print("Harf Notunuz : DD")
else:
    print("Harf Notunuz : FF")