class Buku :
        def __init__(self,judul,pengarang,tahun_terbit,harga,penerbit,rating):
                self.judul = judul
                self.pengarang = pengarang
                self.tahun_terbit = tahun_terbit
                self.harga = harga
                self.penerbit = penerbit
                self.Buku__rating=rating
        
buku = Buku ('Tenggelamnya Kapal Van Der Wijck','HAMKA',1938,50000,'Mizan Pustaka',4) 
t='Buku {} karangan {} pertama kali diterbitkan tahun {} oleh {} dan dipasarkan dengan harga {} rating {} '.format(buku.judul,buku.pengarang,buku.tahun_terbit,buku.penerbit,buku.harga,buku.Buku__rating)
print(t) 

buku1 = Buku ('Kisah Muhammmad Al Fatih ','Fatih',2010,50000,'Gramedia Pustaka',4)
m = 'Buku {} karangan {} pertama kali di terbitkan tahun {} oleh {} dan dipasarkan dengan harga {} rating {} '.format(buku1.judul,buku1.pengarang,buku1.tahun_terbit,buku1.penerbit,buku1.harga,buku1.Buku__rating)
print(m)

buku2 = Buku ('Penaklukan Benteng Konstatinopel','Al FATH',2000,75000,'Mizan Pustaka',4)
z = 'Buku {} karangan {} pertama kali di terbitkan tahun {} oleh {} dan dipasarkan dengan harga {} rating {} '.format(buku2.judul,buku2.pengarang,buku2.tahun_terbit,buku2.penerbit,buku2.harga,buku2.Buku__rating)
print(z)

# saya menambahkan atribut private dengan objek rating pada menu buku 