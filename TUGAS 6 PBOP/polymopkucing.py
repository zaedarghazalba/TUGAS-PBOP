class Kucing:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
 
    def bersuara(self):
        print("Meow")
 
 
class Dog:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
 
    def bersuara(self):
        print("Guk..guk...")
 
kucing1 = Kucing("Tom", 3)
anjing1 = Dog("Spike", 4)
 
for hewan in (kucing1, anjing1):
    hewan.bersuara()