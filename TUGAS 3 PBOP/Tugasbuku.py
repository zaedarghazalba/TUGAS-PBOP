class Buku :
        def __init__(self,judul,pengarang,tahun_terbit,harga,penerbit):
                self.judul = judul
                self.pengarang = pengarang
                self.tahun_terbit = tahun_terbit
                self.harga = harga
                self.penerbit = penerbit
buku = Buku ('Tenggelamnya Kapal Van Der Wijck','HAMKA',1938,50000,'Mizan Pustaka') 
t='Buku {} karangan {} pertama kali diterbitkan tahun {} oleh {} dan dipasarkan dengan harga {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit,buku.penerbit,buku.harga)
print(t) 

buku1 = Buku ('Kisah Muhammmad Al Fatih ','Fatih',2010,50000,'Gramedia Pustaka')
m = 'Buku {} karangan {} pertama kali di terbitkan tahun {} oleh {} dan dipasarkan dengan harga {}'.format(buku1.judul,buku1.pengarang,buku1.tahun_terbit,buku1.penerbit,buku1.harga)
print(m)

buku2 = Buku ('Penaklukan Benteng Konstatinopel','Al FATH',2000,75000,'Mizan Pustaka')
z = 'Buku {} karangan {} pertama kali di terbitkan tahun {} oleh {} dan dipasarkan dengan harga {}'.format(buku2.judul,buku2.pengarang,buku2.tahun_terbit,buku2.penerbit,buku2.harga)
print(z)