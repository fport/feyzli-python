#datetime

from datetime import datetime 
import time
"""
suan = datetime.now()
print(suan.year)
print(suan.month)
print(suan.day)
print(suan.hour)
print(suan.minute)
print(suan.second)
print(suan.date())
print(suan.time())
"""
"""
suan = datetime.now()

liste = str(suan.date()).split("-")

print("Yıl : {}, Ay : {} , Gun {}".format(liste[0],liste[1],liste[2]))
"""

"""
while True:
    suan = datetime.now()
    saniye = suan.second
    
    if(saniye == 20):
        print("saniye 00'a geldi !")
        break
    print(suan)
    time.sleep(1)
   """
   
suan = datetime.now()
print(datetime.ctime(suan).split(" ")[3].split(":"))
   
    
