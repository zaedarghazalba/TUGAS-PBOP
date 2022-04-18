class PerpusItem :
        def __init__(self,judul,subjek,lokasi,info):
                self.judul = judul
                self.subjek = subjek
                self.lokasi = lokasi
                self.info = info

        '''def lokasiSimpan(self):
                self.lokasi = lokasi
                self.info = info
'''
class Buku (PerpusItem) : 
        def __init__ (self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran):
                super().__init__ (judul,'Buku',lokasi,info)
                self.isbn = isbn
                self.pengarang = pengarang 
                self.jmlhal = jmlhal
                self.ukuran = ukuran

class Majalah (PerpusItem):
        def __init__ (self,judul,subjek,lokasi,info,volume,issue):
                super().__init__(judul,'Majalah',lokasi,info)
                self.volume = volume
                self. issue = issue

class DVD (PerpusItem):
        def __init__(self,judul,subjek,lokasi,info,aktor,genre):
                super().__init__(judul,'DVD',lokasi,info)
                self.aktor = aktor
                self. genre = genre

b = Buku ('Pemrograman Python','Buku Cetak','Rak nomor 1','Dipinjam','945-844-98-02','Yogi-Syarif',2,'25x15')
m = Majalah ('Dunia komputer','Majalah cetak','Rak nomor 2','Tersedia','VII','Komputer')
d = DVD('Shingeki No Kiyojin','Softcopy','Rak nomor 3','Tersedia','Mikasa','Anime')

daftar = [b,m,d]
for dft in daftar :
        print('{} {} {} {}'.format(dft.judul,dft.subjek,dft.lokasi,dft.info))