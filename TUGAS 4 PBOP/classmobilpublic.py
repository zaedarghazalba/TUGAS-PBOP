class Mobil():

    # public variabel
    def __init__(self, jendela, pintu, mesin):
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin

audi=Mobil(4,4,"Diesel")
print(audi.pintu,audi.jendela,audi.mesin)

truk=Mobil(6,6,"solar diesel")
print(truk.mesin)