# insert data pada tabel pegawai
import sqlite3


conn = sqlite3.connect('TUGASPBOP.db')
cur = conn.cursor()


# Menambah 3 baris data
cur.execute(
    '''INSERT INTO pegawai VALUES ('0004','ZAEDARGHAZALBA','K04','A4','AKTIF','2')''')
cur.execute(
    '''INSERT INTO gaji VALUES ('januari','0004',30,0,1,0,4,20000)''')
cur.execute(
    '''INSERT INTO golongan VALUES ('A4','ATAS',1000000,500000,300000,250000,300000)''')
cur.execute(
    '''INSERT INTO jabatan VALUES ('K04','MANAGER4',6000000,4000000)''')


# Commit transaksi
conn.commit()

# menutup objek kursor
cur.close()

# menutup objek koneksi
conn.close()
