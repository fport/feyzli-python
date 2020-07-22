import cv2
import numpy as np
"""
resim = cv2.imread("resim.jpg")


cv2.imshow("Tony Soprano",resim)


print(resim[50,50])
print("Resim ozelligi =" + str(resim.shape))
print("Resim boyutu =" + str(resim.size))
print("Resim bit degeri =" + str(resim.dtype))

"""
resim = cv2.imread("resim.jpg")
bolge = resim[100:150,150:250]
resim[0:50,0:100] = bolge
resim[0:50,100:200] = bolge

cv2.imshow("Kesilen Bölge",bolge)
cv2.imshow("Tony Soprano",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()