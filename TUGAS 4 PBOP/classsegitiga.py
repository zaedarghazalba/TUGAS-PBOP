class Segitiga:
     def _init_(self, alas, tinggi):
          self.alas = alas
          self.tinggi = tinggi
          self.luas = 0.5 * alas * tinggi
segitiga_besar = Segitiga(100,80)

# akses variable public :alas, tinggi, dan luas dari kelas segitiga
print("alas: ", segitiga_besar.alas)
print("tinggi:", segitiga_besar.tinggi)
print("luas: ", segitiga_besar.luas)