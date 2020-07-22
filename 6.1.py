"""
r' modu: Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.
'r+' modu: Dosyayı hem okumak hem de yazmak için açar. Eğer çağrılan dosya 
bulunamadıysa yeni bir dosya oluşturulmaz.

'w' modu: Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
'w+' modu: Dosyayı hem okumak hem de yazmak için açar. Varolan dosyanın üzerine yazma
 işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.

'a' modu: Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan
 eklemeye devam eder. Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya 
 oluşturur.
'a+' modu: Dosyayı hem ekleme hem de okuma işlemi için açar. Eğer çağrılan dosya
 bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa yazma ve okuma işlemleri 
 yapacak yeni bir dosya oluşturur.
 
 
dosya = open('metin_dosyasi.txt', 'w')  # w modunda dosyamızı açtık.
Python derleyicisi direkt dosya ismi verdiğimizden dolayı
.py dosyamız ile aynı klasörde bu metin dosyasını arayacaktır.
Eğer böyle bir dosya yok ise, sıfırdan aynı isimle yeni bir dosya
 oluşturacaktır.
satir1 = "bu benim ilk satırım"  # yazdirilacak metin
dosya.write(satir1)  # yazdirma islemi
"""


dosya =open("kayıt.txt","w")

print("1-Porti",file=dosya)
#print("3-Torti",file=dosya,flush = True)
dosya.close()
