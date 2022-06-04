import sqlite3

conn = sqlite3.connect("nsnsdncs")
cur = conn.cursor()

# data sebelum dihapus
for row in cur.execute("SELECT * FROM produk"):
    print('%s,%s,%.0f' % (row[0], row[1], row[2]))

print("-------------------------------------")

# menghapus datanya

cur.execute('''DELETE FROM produk 
                WHERE kode = ? ''', ('P002',))

conn.commit()

# data setelah dihapus
for row in cur.execute("SELECT * FROM produk"):
    print('%s,%s,%.0f' % (row[0], row[1], row[2]))

cur.close()
conn.close()
