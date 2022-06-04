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

cur.close()
conn.close()
