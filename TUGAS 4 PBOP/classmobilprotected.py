class Mobil():
    # protected variabel
    def __init__(self, jendela, pintu, mesin):
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin

class Merekmobil(Mobil):
        def __init__(self, jendela, pintu, mesin):
            super().__init__(jendela, pintu, mesin)

        def tampilkan(self):
                #menampilkan dari subclass
            print(f' {self._jendela}  {self._pintu}  {self._mesin}')

ferrari = Merekmobil(4,4,"Diesel")
ferrari.tampilkan()