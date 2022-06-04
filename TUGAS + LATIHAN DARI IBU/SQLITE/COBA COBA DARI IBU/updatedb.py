import sqlite3

conn = sqlite3.connect("mydbpbop")
cur = conn.cursor()

# before update
for row in cur.execute("SELECT * FROM produk "):
    print('%s,%s,%.0f' % (row[0], row[1], row[2]))

print("------------------------------------")

# update data
cur.execute('''UPDATE produk
                SET harga = ?
                WHERE kode = ? ''', (3000, 'PRODUK1'))

conn.commit()

# after update
for row in cur.execute("SELECT * FROM produk"):
    print('%s,%s,%.0f' % (row[0], row[1], row[2]))

cur.close()
conn.close()
