import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

b,g,r = cv2.split(resim)
yeni_resim = cv2.merge((b,g,r))

cv2.imshow("Tony soprano orijinal",resim)
cv2.imshow("Tony soprano Merge Edilmis REsim",yeni_resim)


cv2.waitKey(0)
cv2.destroyAllWindows()

