import cv2
import numpy as np


resim = cv2.imread("resim.jpg")

#resim[:,:,0]=255
#resim[:,:,1]=255
#resim[:,:,2]=255

resim[50:100,100:150,0]=255

cv2.imshow("Tony Soprano Orijinal",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()