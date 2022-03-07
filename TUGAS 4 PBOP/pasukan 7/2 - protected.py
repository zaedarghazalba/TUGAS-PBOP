class Utama:
    def __init__(self):
        self._a = 2


class Turunan(Utama):
    def __init__(self):
        

        # memanggil konstruktor pada kelas utama
        Utama.__init__(self)
        print("Memanggil variabel protected pada class utama : ", self._a)


        # modify
        self._a= 3
        print("Memanggil variabel protected yang di modifikasi diluar class :", self._a)

objek1 = Turunan()
objek2 = Utama()

# memanggil variabel utama
print("Memanggil variabel protected pada objek1 :", objek1._a)
print("Memanggil variabel protected pada objek1 :", objek2._a)
