import cv2
import numpy as np

def main():
    feyyaz_yigit = cv2.imread("feyyaz_yigit.jpg")
    android = cv2.imread("android.jpg")
    
    a_gri = cv2.cvtColor(android,cv2.COLOR_BGR2GRAY)
    yükseklik,genislik,kanal =android.shape

    ROI = feyyaz_yigit[0:yükseklik,0:genislik]
    
    
    ret,mask = cv2.threshold(a_gri,10,255,cv2.THRESH_BINARY)
    mask_inver = cv2.bitwise_not(mask)
    
    feyyazarka = cv2.bitwise_and(ROI,ROI,mask = mask_inver)
    
    toplam = cv2.add(feyyazarka,android)
   # cv2.imshow("Toplam",toplam)
    
    feyyaz_yigit[0:yükseklik,0:genislik] = toplam
    cv2.imshow("Son Hali",feyyaz_yigit)

    """
    cv2.imshow("Feyyaz Arka",feyyazarka)
    
    cv2.imshow("Feyyaz Yigit",feyyaz_yigit)
    cv2.imshow("Android",android)
    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()