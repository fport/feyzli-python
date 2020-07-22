import cv2
import numpy as np

def main():
    resim = cv2.imread("android.jpg")
    
    print(resim.shape)
    iki_kat = cv2.pyrUp(resim)
    iki_kat_kucuk = cv2.pyrDown(resim)

    cv2.imshow("Resim",resim)
    cv2.imshow("İki Kat Büyük",iki_kat)
    cv2.imshow("iki Kat Kucuk",iki_kat_kucuk)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ =="__main__":
    main()
        
    