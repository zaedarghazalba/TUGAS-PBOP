from connect import db, cursor

# suplier
cursor.execute("SELECT * FROM `suplier`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])) 

# barang
cursor.execute("SELECT * FROM `barang`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# nota
cursor.execute("SELECT * FROM `nota`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))

# transaksi
cursor.execute("SELECT * FROM `transaksi`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))

db.commit()