import cv2
import numpy as np 
 
resim = cv2.imread("barbara.jpg")

yuz = resim[0:250,400:600]

print(resim.shape)

cv2.imshow("Barbara Palvin",resim)
cv2.imshow("Barbara Palvin Yüz",yuz)

 
cv2.waitKey(0)
cv2.destroyAllWindows
