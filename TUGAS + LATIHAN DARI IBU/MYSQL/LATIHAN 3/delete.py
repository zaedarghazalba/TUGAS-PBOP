from connect import db, cursor

# suplier
cursor.execute("DELETE FROM `suplier`")

# barang
cursor.execute("DELETE FROM `barang`")

# nota
cursor.execute("DELETE FROM `nota`")

# transaksi
cursor.execute("DELETE FROM `transaksi`")

db.commit()