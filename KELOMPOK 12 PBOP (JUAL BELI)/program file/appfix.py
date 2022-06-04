import time
host = "localhost"
user = "root"




import mysql.connector as mysql

def getDate():
            import datetime
            now=datetime.datetime.now
            return str(now().date())

def getTime():
            import datetime
            now=datetime.datetime.now
            return str(now().time())


db = mysql.connect(
    host = host,
    user = user,
)


cursor = db.cursor()
db.database = "cobamenu"


class menuMakanan:
    def tambahMenu(self,menu_makanan, harga):
        self.menu_makanan = menu_makanan
        self.harga = harga
        
        cursor.execute(f'INSERT INTO `data_makanan` (`menu_makanan`, `harga`) VALUES ("{self.menu_makanan}", "{self.harga}")')
        db.commit()

    def lihatMenu(self):
        menu = "SELECT * FROM data_makanan"
        cursor.execute(menu)
        for row in cursor.fetchall():
            print(row)

class beli:
    def pilihMenu(self):
        order = 'Y'
        global total, data_order, nama
        data_order = []
        nama = ""
        total = 0
        
        while(order == 'y' or order == 'Y'):
            if(nama == ""):
                nama = input("Masukkan nama pemesan:")
            
            print('********** PILIH MAKANAN ********** \n')
            pilihMkn = int(input('Input ID Menu Yang Anda Inginkan: '))
            query = cursor.execute(f"SELECT * FROM data_makanan WHERE id = '{pilihMkn}' ")
            cursor.execute(query)

            x = cursor.fetchall()[0]
            total += x[2]

            data_order.append(x)
            
            order = str(input('Ingin Pesan Lagi? [Y/N]: '))
        
        print('\n--------------- TOTAL PESANAN YANG HARUS ANDA BAYAR ---------------')
        print('Total harga pesanan: Rp',total)

    def bayarMkn(self):
        global bayarMnu, kembalian
        bayarMnu = int(input('\nMasukkan nominal yang dibayarkan : Rp'))
        
       
        

        while bayarMnu < total:
            print("Nominal yang anda masukkan tidak mencukupi untuk melakukan pembayaran")
            bayarMnu = int(input('\nSilahkan masukkan nominal bayar lagi : Rp'))

        kembalian = bayarMnu - total
        print('\n####### Transaksi Berhasil Dilakukan #######')

    def listmakan(self):
        menu_makan = data_order
        print(*menu_makan, sep = '\n')

    
        
    def strukMkn(self):
            timestr = time.strftime("%H_%M_%S")
            admin = input("Masukkan nama admin = ")

            a = open("STRUK-"+admin+timestr+"-.txt", "w+")

            a.write(f'''
            
========== RESTO BAROKAH =========\n 

NAMA PEMESAN = {nama}

''')        
            a.write("MENU PESANAN = \n")
            for i in data_order:
                a.write(f"{i}\r")

            a.write(f''' 

=================================\n
TANGGAL     = {getDate()}
WAKTU       = {getTime()}\n
=================================\n   
TOTAL BAYAR = {total}
PEMBAYARAN  = {bayarMnu}     
KEMBALIAN   = {kembalian}\n
=================================

''')
            a.close()

            
    
    def keluar(self):
        print('\n---------- TERIMA KASIH SILAHKAN DATANG KEMBALI ----------')

class Laporan(beli) :
        def laporan (self):
                with open("laporan.txt", "a+") as f:
                        f.write("PEMASUKAN TANGGAL ="+getTime()+",SEBESAR =Rp"+str(total)+"\n")
        
pembelian = beli
m = menuMakanan()
b = beli()
c = Laporan ()

while True:
    print('\n----> RESTO BAROKAH SYSTEM <----')
    print('1. Tambah Menu Makanan')
    print('2. Lihat Menu Makanan')
    print('3. Pilih Menu')
    print('4. Lihat Menu Yang Anda Pesan')
    print('5. Bayar Makanan')
    print('6. Cetak Struk + update laporan')
    print('0. Keluar Program')

    pilihan = input('\nMasukkan Pilihan Menu Anda : ')

    if pilihan == '1':
        makanan             = str(input('Input menu makanan yang ingin ditambahkan: '))
        harga_makanan       = int(input('Input harga menu makanan yang ditambahkan: '))
        m.tambahMenu(makanan,harga_makanan)

    elif pilihan == '2':
        m.lihatMenu()

    elif pilihan == '3':
        m.lihatMenu()
        b.pilihMenu()

    elif pilihan == '4':
        b.listmakan()

    elif pilihan == '5':
        b.bayarMkn()
        
    elif pilihan == '6':
        b.strukMkn()
        c.laporan()
    elif pilihan == '0':
        b.keluar()
        break