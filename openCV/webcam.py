import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,kare = kamera.read()
    cv2.rectangle(kare,(0,0),(100,100),(255,255),)
    
    cv2.imshow("Video",kare)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows