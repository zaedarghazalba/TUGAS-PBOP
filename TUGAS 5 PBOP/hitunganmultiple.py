#  MULTIPLE INHERITENCE
class Perhitungan:
    def penjumlahan(self, a, b):
        return a + b

class Perhitungan2:
    def perkalian(self, a, b):
        return a * b

class Hitung(Perhitungan,Perhitungan2):
    def pembagian(self, a, b):
        return a/b

h = Hitung()
print(h.penjumlahan(30,30))
print(h.perkalian(8,4))
print(h.pembagian(40,20))
