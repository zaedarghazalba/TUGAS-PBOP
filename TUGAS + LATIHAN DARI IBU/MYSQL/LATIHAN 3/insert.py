from connect import db, cursor

# suplier
cursor.execute("INSERT INTO `suplier` (`kode_suplier`, `nama_suplier`) VALUES ('AGE', 'Esa Age Gian Putra')")

# barang
cursor.execute("INSERT INTO `barang` (`kode_barang`, `nama_barang`) VALUES ('B-123', 'Roma kelapa')")

# nota
cursor.execute("INSERT INTO `nota` (`nomer_nota`, `tanggal`, `tempo`, `total`, `kode_suplier`) VALUES ('712891', '2022-05-25', '2022-05-25', '90000000', 'AGE')")

# transaksi
cursor.execute("INSERT INTO `transaksi` (`nomer_nota`, `kode_barang`, `quantity`, `harga`) VALUES ('712891', 'B-123', '10', '90000000')")

db.commit()