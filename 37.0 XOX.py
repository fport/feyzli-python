"""
XoX Game

"""

class XOX():
    def __init__(self,tahta = [[" "," "," "],[" "," "," "],[" "," "," "]]):
        self.tahta = tahta
        self.oyunDurum = True

    def tahtaGöster(self):
        for i in self.tahta:
            print(i)

    def p1Secim(self):
        satir = int(input("P1 >> Satir Giriniz : "))
        sutun = int(input("P1 >> Sutun Giriniz : "))
        if self.kontrol(satir,sutun):
            self.tahta[satir-1][sutun-1] = "X"
        else:
            print("Girdiginiz Bölge Dolu !")
            self.p1Secim()

    def p2Secim(self):
        satir = int(input("P2 >> Satir Giriniz :"))
        sutun = int(input("P2 >> Sutun Giriniz :"))
        if self.kontrol(satir,sutun):
            self.tahta[satir-1][sutun-1] = "O"
        else:
            print("Girdiginiz Bölge Dolu !")
            self.p2Secim()

    def durum(self):
        if(self.tahta[0][0] == "X"and self.tahta[0][1] == "X" and self.tahta[0][2] == "X"):
            self.oyunDurum = True
        if(self.tahta[1][0] == "X" and self.tahta[1][1] == "X"and self.tahta[1][2] == "X"):
            self.oyunDurum = True
        if(self.tahta[2][0] == "X" and self.tahta[2][1] == "X" and self.tahta[2][2] == "X"):
            self.oyunDurum = True
        if(self.tahta[0][0] == "X"and self.tahta[1][0] == "X" and self.tahta[2][0] == "X"):
            self.oyunDurum = True
        if(self.tahta[0][1] == "X"and self.tahta[1][1] == "X" and self.tahta[2][1] == "X"):
            self.oyunDurum = True
        if(self.tahta[0][2] == "X"and self.tahta[1][2] == "X" and self.tahta[2][2] == "X"):
            self.oyunDurum = True
        if (self.tahta[0][0]== "X" and self.tahta[1][1]== "X"and self.tahta[2][2] == "X"):
            self.oyunDurum = True
        if (self.tahta[0][2]== "X" and self.tahta[1][1]== "X" and self.tahta[2][0] == "X"):
            self.oyunDurum = True
        if (self.tahta[0][0] == "O"and self.tahta[0][1] == "O"and self.tahta[0][2] == "O"):
            self.oyunDurum = True
        if (self.tahta[1][0]== "O" and self.tahta[1][1] == "O" and self.tahta[1][2] == "O"):
            self.oyunDurum = True
        if (self.tahta[2][0] == "O" and self.tahta[2][1] == "O" and self.tahta[2][2] == "O"):
            self.oyunDurum = True
        if (self.tahta[0][0] == "O" and self.tahta[1][0] == "O" and self.tahta[2][0] == "O"):
            self.oyunDurum = True
        if (self.tahta[0][1] == "O" and self.tahta[1][1] == "O" and self.tahta[2][1] == "O"):
            self.oyunDurum = True
        if (self.tahta[0][2] == "O" and self.tahta[1][2] == "O" and self.tahta[2][2] == "O"):
            self.oyunDurum = True
        if (self.tahta[0][0] == "O" and self.tahta[1][1] == "O" and self.tahta[2][2] == "O"):
            self.oyunDurum = True
        if (self.tahta[0][2] == "O" and self.tahta[1][1] == "O" and self.tahta[2][0] == "O"):
            self.oyunDurum = True
        return False

    def kontrol(self,satir,sutun):
        if(self.tahta[satir-1][sutun-1] != " "):
            return False
        else:
            return True

xox = XOX()

while True:
    xox.tahtaGöster()
    xox.p1Secim()
    xox.tahtaGöster()
    if xox.durum():
        print(">> P1 Kazandi <<")
        break
    xox.p2Secim()
    if xox.durum():
        print(">> P2 Kazandi <<")
        xox.tahtaGöster()
        break

