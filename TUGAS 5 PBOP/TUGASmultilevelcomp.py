# Multilevel
class ComputerPart():
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, jenis ,harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga
    
class HardDiskSATA(Processor):
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga

class RandomAccessMemory(HardDiskSATA):
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga
    
classawal   = ComputerPart('Enter Komputer', 'PC DEWA KIPAS LIBAS ',40000000,'spek : ')
proci   = Processor('INTEL ni boss',  'Core i7 7740X', 328000, '4GHz dan 4 Mb chache')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB dan 7200 Rpm')
randomacc   = RandomAccessMemory('Corsair', 'RAM', 2346000, '10GB x 2 total 20GB DDR 4 3400 MHz')
parts = [classawal,proci,hdd,randomacc]
for x in parts:
    print('{} dengan harga {} produksi {} dengan {}'.format(x.nama,x.jenis,x.pabrikan,x.harga))