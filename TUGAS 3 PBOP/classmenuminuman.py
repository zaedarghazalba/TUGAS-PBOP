class MenuMinuman :
        def __init__(self,nama,deskripsi,harga ) :
                self.nama = nama
                self.deskripsi = deskripsi
                self.harga = harga 

mnm1 = MenuMinuman ('Jus Jambu','Jus Jambu Merah tanpa gula',8500)
mnm2 = MenuMinuman ('Jus Alpukat Original','Jus Alpukat dengan tambahan air gula merah',15000)
mnm3 = MenuMinuman ('Jus Alpukat Xtra Milk','Jus Alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000)
mnm4 = MenuMinuman ('Red & Smooth','Smoothie Pisang Susu Dengan Strawberry syrup',17500)

pilihan_minuman = [mnm1,mnm2,mnm3,mnm4]
print ('Daftar menu healthy fruits')
for mn in pilihan_minuman :
        t = '{} harga Rp {}, {}'. format (mn.nama,mn.harga,mn.deskripsi)
        print(t)
             