class MenuMinuman :
        def __init__(self,nama,deskripsi,harga,ratingmnmn) :
                self.nama = nama
                self.deskripsi = deskripsi
                self.harga = harga 
                self.Menuminuman__rating = ratingmnmn
                

mnm1 = MenuMinuman ('Jus Jambu','Jus Jambu Merah tanpa gula',8500,4.5)
mnm2 = MenuMinuman ('Jus Alpukat Original','Jus Alpukat dengan tambahan air gula merah',15000,5)
mnm3 = MenuMinuman ('Jus Alpukat Xtra Milk','Jus Alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000,4)
mnm4 = MenuMinuman ('Red & Smooth','Smoothie Pisang Susu Dengan Strawberry syrup',17500,4)
toping1 = MenuMinuman ('toping 1','tambah toping oreo crunch =', 5000,4)
toping2 = MenuMinuman ('toping 2','tambah potongan jely dan buah segar =', 5000,4)
toping3 = MenuMinuman ('toping 3','tambahan taburan coklat bubuk = ',2000,4)
size1 = MenuMinuman ('size 1','Jumbo = +',8000,5)
size2 = MenuMinuman ('size 2','Medium = +',4000,4)


pilihan_minuman = [mnm1,mnm2,mnm3,mnm4]
print ('Daftar menu healthy fruits')
for mn in pilihan_minuman :#penambhana atribut private 
        t = '{} harga Rp {}, {} dengan rating {}'. format (mn.nama,mn.harga,mn.deskripsi,mn.Menuminuman__rating)
        print(t)
pilihan_toping = [toping1,toping2,toping3]
print('Daftar toping yang tersedia')
for top in pilihan_toping :
        tp = '{}''{}''{} dengan rating penjualan {}'.format(top.nama,top.deskripsi,top.harga,top.Menuminuman__rating)
        print(tp)
pilihan_size =[size1,size2]
print('Daftar ukuran minuman ')
for siz in pilihan_size:
        sz = '{}''{}''{} dengan rating penjualan {}'.format(siz.nama,siz.deskripsi,siz.harga,siz.Menuminuman__rating)
        print(sz)
             
#saya menambahkan atribut private pada objek minuman , toping ,dan size 
