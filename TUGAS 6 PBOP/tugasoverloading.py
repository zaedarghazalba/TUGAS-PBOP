#TUGAS OVERLOADING

print("Bentuk Overloading class computerpart")

class ComputerPart:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga
    #METHODE OVERLOADING DAN TAMBAHAN VALIDASI DISKON
    def diskon (self,totalbayar=None,harga=None):
        if totalbayar !=None and harga != None :
                jmlhbarang = harga
                print("jumlah barang :",totalbayar)
                print("jumlah bayar : ",jmlhbarang)
                self.ketdiskon(jmlhbarang) 
        else :
                jmlhbarang = totalbayar
                print("jumlah barang :",totalbayar)
                print("jumlah bayar :",jmlhbarang)
                self.ketdiskon(jmlhbarang)
    
    def ketdiskon (self,totalbayar):
            if totalbayar > 500000 :
                    print ("selamat anda mendapat diskon tahun baru")
            else :
                    print("anda tidak dapat diskon ")
   
    

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        super().__init__(pabrikan,nama,"Processor",harga)
        self.jumlah_core = jumlah_core
        self.speed       = speed

class RandomAccessMemory(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas
        self.rpm       = rpm
    


p = Processor("AMD","Ryzen 3 3250U",3500000,2,"2.6 GHz")
r = RandomAccessMemory("Corsaire","DDR4 SODIMM PC19200/2400 MHz",990000,"8 GB")
hdd = HardDiskSATA("Toshiba","HDD 2.5 inch",295000,"500 GB",7200)

p.diskon(1,p.harga)

r.diskon(1,r.harga)

hdd.diskon(1,hdd.harga)

part = [p,r,hdd]
for z in part:
    print('\n{} {} produksi {} berharga {}'.format(z.jenis,z.nama,z.pabrikan,z.harga))