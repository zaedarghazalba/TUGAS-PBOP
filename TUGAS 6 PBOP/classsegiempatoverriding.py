class Segiempat():
    def _init_(self, panjang, lebar):
        self.panjang=panjang
        self.lebar=lebar

    

    def hitungLuas(self): # Method Overriding
        print("Luas Segiempat =", self.panjang * self.lebar, "m*2")

class Bujursangkar(Segiempat):
    def _init_(self,sisi):
        self.side=sisi
        Segiempat._init_(self,sisi,sisi)

    def hitungluas(self): # Method Overriding
        print("Luas Bujur sangkar =", self.side*self.side, "m*2")

b=Bujursangkar(4)
s=Segiempat (2,4)
b.hitungLuas()
s.hitungLuas()