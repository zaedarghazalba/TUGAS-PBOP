import sqlite3

conn = sqlite3.connect("mydbpbop")
cur = conn.cursor()
result = cur.execute("SELECT * FROM produk")

# membaca data
for row in result:
    print('%s,%s,%.0f' % (row[0], row[1], row[2]))

cur.close()
conn.close()
