from connect import db, cursor

# suplier
cursor.execute("UPDATE `suplier` SET `kode_suplier`='NFL',`nama_suplier`='Naufal Firmansyah' WHERE kode_suplier = 'AGE'")

# barang
cursor.execute("UPDATE `barang` SET `kode_barang`='A-321',`nama_barang`='Biskuit Khong Guan' WHERE kode_barang = 'B-123'")

# nota
cursor.execute("UPDATE `nota` SET `nomer_nota`=12345,`tanggal`='2022-05-30',`tempo`='2022-05-30',`total`='10000000',`kode_suplier`='NFL' WHERE nomer_nota = 712891")

# transaksi
cursor.execute("UPDATE `transaksi` SET `nomer_nota`='120129',`kode_barang`='A-123',`quantity`=10,`harga`='5000000' WHERE nomer_nota = 712891")

db.commit()