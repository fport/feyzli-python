from datetime import datetime
import os


zaman_dam = os.stat("C:/Users/porti/Desktop/belge.txt").st_mtime

tarih = datetime.fromtimestamp(zaman_dam)

suan = datetime.now()
"""
neKadarOldu = suan - tarih
print(neKadarOldu)
"""
"""
suan_dakika = suan.minute

dosya_dakika = tarih.munite

fark = suan_dakika - dosya_dakika

print("Dosya tam olarak {} dk once olusturulmus".format(fark))
"""
suan = datetime.now()
tarih = datetime(2020,1,31)
fark = suan-tarih
print(fark)
print()