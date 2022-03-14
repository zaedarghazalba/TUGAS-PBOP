# Multiple
class ComputerPart():
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga

class Processor():
    def __init__(self, jumlah_core, speed,):
        self.jumlah_core = jumlah_core
        self.speed       = speed
        
        
class RandomAccessMemory():
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas

class HardDiskDATA():
    def __init__(self,rpm):
        self.rpm = rpm
        

class Computer( ComputerPart, Processor, RandomAccessMemory, HardDiskDATA ):
    def __init__(self, pabrikan, nama, jenis, harga, jumlah_core, speed, kapasitas, rpm):
        ComputerPart.__init__(self, pabrikan, nama, jenis, harga)
        Processor.__init__(self, jumlah_core, speed, )
        RandomAccessMemory.__init__(self, kapasitas)
        HardDiskDATA.__init__(self, rpm)

pcsultan= Computer('INTEL', 'ASUS ROG', 'CORE I9', 1000, 8, '7Ghz', '1000GB', '7200 RPM')
pcdewa = Computer('Intel', 'Lenovo Legion','CORE I7', 1500, 6, '6Ghz', '500GB', '7200 RPM')
pcmahasiswa= Computer('INTEL', 'Ideapad Gaming Budget', 'CORE I5', 4, 3000, '5Ghz', '100GB', '7200 RPM')

u = [pcsultan,pcdewa,pcmahasiswa]
for o in u: 
    print('Pabrikan: {}\nNama: {}\nJenis: {}\nJumlah_core: {}\nSpeed: {}\nKapasitas: {}\nRPM : {} \n\n'.format(o.pabrikan,o.nama,o.harga,o.jumlah_core,o.speed,o.kapasitas,o.rpm))
      