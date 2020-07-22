import datetime 
import os

artis  = datetime.timedelta(days = 200)
simdi = datetime.datetime.now()
belirtilen_tarih = simdi + artis

print(datetime.datetime.strftime(belirtilen_tarih,("%B %Y")))
