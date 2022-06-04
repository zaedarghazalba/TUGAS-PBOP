import sqlite3

conn = sqlite3.connect("TUGASPBOP.db")
cur = conn.cursor()


print("--------PEGAWAI------------")

# membaca data pegawai
pegawainya = cur.execute("SELECT * FROM pegawai")
for row in pegawainya:
    print('%s,%s,%s,%s,%s,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


print("--------GAJI------------")

# membaca data GAJI
gajinya = cur.execute("SELECT * FROM gaji")
for row in gajinya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


print("--------JABATAN------------")

# membaca data JABATAN
jabatannya = cur.execute("SELECT * FROM jabatan")
for row in jabatannya:
    print('%s,%s,%.0f,%.0f' % (row[0], row[1], row[2], row[3]))


print("--------GOLONGAN------------")

# membaca data GOLONGAN
golongannya = cur.execute("SELECT * FROM golongan")
for row in golongannya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


# menghapus data pegawai
a = input('masukkan nip yang ingin anda hapus data pegawainya  :')
cur.execute('''DELETE FROM pegawai
                WHERE nip = ? ''', (a,))

# conn.commit()

# menghapus data gaji
b = input('masukkan nip yang ingin anda hapus data gaji  :')
cur.execute('''DELETE FROM gaji 
                WHERE nip = ? ''', (b,))

conn.commit()

# menghapus data jabatan
c = input('masukkan kode_jabatan yang ingin anda hapus data jabatan  :')
cur.execute('''DELETE FROM jabatan 
                WHERE kode_jabatan = ? ''', (c,))

conn.commit()

# menghapus data golongan
d = input('masukkan kode_golongan yang ingin anda hapus data golongan  :')
cur.execute('''DELETE FROM golongan 
                WHERE kode_golongan = ? ''', (d,))

conn.commit()


print("--------PEGAWAI------------")

# before update
pegawainya = cur.execute("SELECT * FROM pegawai")
for row in pegawainya:
    print('%s,%s,%s,%s,%s,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5]))

print("--------GAJI------------")

# membaca data GAJI
gajinya = cur.execute("SELECT * FROM gaji")
for row in gajinya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


print("--------JABATAN------------")

# membaca data JABATAN
jabatannya = cur.execute("SELECT * FROM jabatan")
for row in jabatannya:
    print('%s,%s,%.0f,%.0f' % (row[0], row[1], row[2], row[3]))


print("--------GOLONGAN------------")

# membaca data GOLONGAN
golongannya = cur.execute("SELECT * FROM golongan")
for row in golongannya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


cur.close()
conn.close()
