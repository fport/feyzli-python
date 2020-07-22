import cv2
import numpy as np

def main():
    
    feyyaz_yigit = cv2.imread("feyyaz_yigit.jpg")
    android = cv2.imread("android.jpg")
    
    
    a_gri = cv2.cvtColor(android,cv2.COLOR_BGR2GRAY)
        
    yukseklik,genislik,kanal = android.shape
    print(yukseklik,genislik,kanal)
    
    ROI = feyyaz_yigit[0:yukseklik,0:genislik]
    cv2.imshow("ROI",ROI)
    
    ret,mask = cv2.threshold(a_gri,10,255,cv2.THRESH_BINARY)  #belli piksel degeri ustunun 255 veya 0 yapma 
    
    mask_inver = cv2.bitwise_not(mask)
    
    feyyazarka = cv2.bitwise_and(ROI,ROI,mask = mask_inver)
  
    cv2.imshow("Feyyaz Arka ",feyyazarka)
    cv2.imshow("aa",feyyaz_yigit)

    cv2.imshow("Ters Masklanmis Resim",mask_inver)
    cv2.imshow("Masklanmıs Resim ",mask)
    cv2.imshow("Feyyaz Yigit",feyyaz_yigit)
    cv2.imshow("Android",a_gri)



    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
