import cv2
import numpy as np

resim = cv2.imread("barbara.jpg")

# >> Resmi uzatma

uzatılan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

# >> Resmi aynalama

aynalanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

# >> Resmi tekrar etme

tekrarlanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

# >> Resmi etrafını sarma

sarilan_resim = cv2.copyMakeBorder(resim,20,20,20,20,cv2.BORDER_CONSTANT,value = [0,0,255] )

cv2.imshow("Barbara Palvin Orijinal",resim)
cv2.imshow("Barbara Palvin Uzatma",uzatılan_resim)
cv2.imshow("Barbara Palvin Aynalama",aynalanan_resim)
cv2.imshow("Barbara Palvin Tekrarlama",tekrarlanan_resim)
cv2.imshow("Barbara Palvin Sarma",sarilan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
