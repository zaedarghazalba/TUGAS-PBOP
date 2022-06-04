from connect import db, cursor

# dosen
cursor.execute("INSERT INTO `dosen` (`kode_dos`, `nama_dos`, `alamat_dos`, `no_telp`) VALUES ('FDLIND', 'Fadil Indra Sanjaya', 'Sleman Yogyakarta', '085815887425')")

# kuliah
cursor.execute("INSERT INTO `kuliah` (`kode_mk`, `kode_dos`, `waktu`, `tempat`) VALUES ('HK-123', 'FDLIND', '15:23:50', 'LK 2.2')")

# jabatan
cursor.execute("INSERT INTO `mata_kuliah` (`kode_mk`, `nama_mk`, `sks`, `semester`) VALUES ('HK-123', 'Hukum Bernegara', '3', '4')")

db.commit()