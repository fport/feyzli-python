import cv2
import numpy as np

def main():
    resim1 = cv2.imread("x.jpg")
    resim2 = cv2.imread("y.jpg")
 
    toplam = cv2.add(resim1,resim2)
   
    print(toplam[200,200])
    print("\n")

    
 
    
    
    agırlıklı_toplam = cv2.addWeighted(resim1,0.2,resim2,0.8,0)
    
    print(agırlıklı_toplam[200,200])
    
    
    cv2.imshow("resim1",resim1)
    cv2.imshow("resim2",resim2)
    cv2.imshow("toplam",toplam)
    cv2.imshow("agırlıklı toplam",agırlıklı_toplam)
    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ =="__main__":
    main()
    
    