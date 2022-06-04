from connect import db, cursor

# dosen
cursor.execute("UPDATE `dosen` SET `kode_dos`='JKSSNT',`nama_dos`='Joko Susanto',`alamat_dos`='Bantul',`no_telp`='0851238791' WHERE kode_dos = 'FDLIND'")

# kuliah
cursor.execute("UPDATE `gaji` SET `bulan`='FEBRUARI',`nip`=1234678910,`masuk`='25',`sakit`=1,`ijin`=0,`alpha`=0,`lembur`=5,`potongan`=1000000 WHERE bulan = 'JANUARI'")

# mata kuliah
cursor.execute("UPDATE `mata_kuliah` SET `kode_mk`='RWP-321',`nama_mk`='Rekayasa Web Praktik',`sks`=2,`semester`=2 WHERE kode_mk = 'HK-123'")

db.commit()