import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

b,g,r = cv2.split(resim)


cv2.imshow("Tony Soprano Orijinal",resim)
cv2.imshow("Tony Soprano Blue",b)
cv2.imshow("Tony Soprano Green",g)
cv2.imshow("Tony Soprano Red",r)


cv2.waitKey(0)
cv2.destroyAllWindows() 