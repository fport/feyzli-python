#Agırlıklı Toplama

import cv2
import numpy as np

def main():
    resim1 = cv2.imread("x.jpg")
    resim2 = cv2.imread("y.jpg")
  
    print(resim1[200,200])
    print(resim2[200,200])
    
    print(resim1[200,200] + resim2[200,200])
    
    print("On Yuz Resim Degerleri: {}, Genişlik {} , Kanal Sayisi {}".format(resim1.shape[0],resim1.shape[1],resim1.shape[2]))
    print("On Yuz Resim Degerleri: {}, Genişlik {} , Kanal Sayisi {}".format(resim2.shape[0],resim2.shape[1],resim2.shape[2]))
        
    cv2.imshow("X.jpg",resim1)
    cv2.imshow("Y.jpg",resim2)

    
   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
    
