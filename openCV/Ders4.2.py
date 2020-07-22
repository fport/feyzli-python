import cv2
import numpy as np

resim = cv2.imread("barbara.jpg")

cv2.rectangle(resim,(600,250),(300,20),[0,0,255],2)


cv2.imshow("Barbara Palvin",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
