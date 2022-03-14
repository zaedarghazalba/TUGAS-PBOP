# Hierarchical 
class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed       = speed
# masih menggunakan super() karena pusatnya ada di computer part
class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas
# masih menggunakan super() karena pusatnya ada di computer part
class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm       = rpm
# masih menggunakan super() karena pusatnya ada di computer part
class Input(ComputerPart):
    def __init__(self, pabrikan, nama, harga, mouse):
        super().__init__(pabrikan, nama, 'Mouse', harga)
        self.mouse = mouse
# masih menggunakan super() karena pusatnya ada di computer part
p    = Processor('Intel', 'Core i7 7740X',4350000, 4,'4.2GHz')
m    = RandomAccessMemory('Corsair', 'DDR4 SODimm PC19200/3400MHz', 328000, '4GB X 2 keping')
hdd  = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
i    = Input('Fantech', 'Thor X9', 600000, 'sensor pixel LG054')

parts = [p,m,hdd,i]
for x in parts:
    print('{} {} produksi {}'.format(x.jenis, x.nama, x.pabrikan))
