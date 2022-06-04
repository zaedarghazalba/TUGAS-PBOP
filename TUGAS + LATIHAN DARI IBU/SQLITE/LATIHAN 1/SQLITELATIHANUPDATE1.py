import sqlite3

conn = sqlite3.connect("TUGASPBOP.db")
cur = conn.cursor()


print("-----------GAJI-------------")


# before update
gajinya = cur.execute("SELECT * FROM gaji")
for row in gajinya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# update data
cur.execute('''UPDATE gaji
                SET potongan = ?
                WHERE nip = ? ''', (30000, '1'))

conn.commit()

# after update
gajinya = cur.execute("SELECT * FROM gaji")
for row in gajinya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


print("------------JABATAN----------------")

# before update
jabatannya = cur.execute("SELECT * FROM jabatan")
for row in jabatannya:
    print('%s,%s,%.0f,%.0f' % (row[0], row[1], row[2], row[3]))

# update data
cur.execute('''UPDATE jabatan
                SET gapok = ?
                WHERE kode_jabatan = ? ''', (8000000, 'K01'))
conn.commit()

# after update
jabatannya = cur.execute("SELECT * FROM jabatan")
for row in jabatannya:
    print('%s,%s,%.0f,%.0f' % (row[0], row[1], row[2], row[3]))


print("-------------GOLONGAN-----------------")

# before update
golongannya = cur.execute("SELECT * FROM golongan")
for row in golongannya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# update data
cur.execute('''UPDATE golongan
                SET tunjangan_anak = ?
                WHERE kode_golongan = ? ''', (1500000, 'A1'))
conn.commit()

# before update
golongannya = cur.execute("SELECT * FROM golongan")
for row in golongannya:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print("-------------PEGAWAI----------------")

# before update
pegawainya = cur.execute("SELECT * FROM pegawai")
for row in pegawainya:
    print('%s,%s,%s,%s,%s,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5]))

# update data
cur.execute('''UPDATE pegawai
                SET jumlah_anak = ?
                WHERE nip = ? ''', (2, '0001'))
conn.commit()

# before update
pegawainya = cur.execute("SELECT * FROM pegawai")
for row in pegawainya:
    print('%s,%s,%s,%s,%s,%.0f' %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


cur.close()
conn.close()
