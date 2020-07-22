import cv2
import numpy as np

resim = cv2.imread("muslum.jpg",0)

print(resim.item(400,200),0) #Blue
print(resim.item(400,200),1) #green
print(resim.item(400,200),2) #red

cv2.imshow("Muslum Baba",resim)

#print(resim.size)
#print(resim.shape)



cv2.waitKey(0)
cv2.destroyAllWindows()