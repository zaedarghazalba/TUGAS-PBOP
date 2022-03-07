class Hitung:
    def __init__(self):
        self._angkaRahasia = 0


    def tampilkanHitung(self):
        self._angkaRahasia += 1
        print(self._angkaRahasia)


        # modify

hitungan = Hitung()
hitungan.tampilkanHitung()


