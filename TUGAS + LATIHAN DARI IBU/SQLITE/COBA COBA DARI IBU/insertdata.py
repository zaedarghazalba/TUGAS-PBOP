import sqlite3

conn=sqlite3.connect("mydbpbop")
cur=conn.cursor()

# Menambah 3 baris data 
cur.execute("INSERT INTO produk VALUES ('PRODUK1','PENSIL',6000)")
cur.execute("INSERT INTO produk VALUES ('PRODUK2','PULPEN',4000)")
cur.execute("INSERT INTO produk VALUES ('PRODUK3','PENGGARIS',8000)")

#Commit transaksi
conn.commit()

#menutup objek kursor
cur.close()

#menutup objek koneksi
conn.close()
