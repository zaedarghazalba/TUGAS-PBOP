class Mobil():
    # private variabel
    def __init__(self, jendela, pintu, mesin):
        self.Mobil__jendela = jendela
        self.Mobil__pintu = pintu
        self.Mobil__mesin = mesin
audi=Mobil(4,4,"Diesel")
print(audi.Mobil__pintu,audi.Mobil__jendela,audi.Mobil__mesin)

truk=Mobil(6,6,"solar diesel")
print(truk.Mobil__mesin)



