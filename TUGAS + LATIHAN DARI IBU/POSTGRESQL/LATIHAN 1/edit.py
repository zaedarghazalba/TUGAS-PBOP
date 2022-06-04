from connect import db, cursor

# gaji
cursor.execute("UPDATE `gaji` SET `bulan`='FEBRUARI',`nip`=1234678910,`masuk`='25',`sakit`=1,`ijin`=0,`alpha`=0,`lembur`=5,`potongan`=1000000 WHERE bulan = 'JANUARI'")

# golongan
cursor.execute("UPDATE `golongan` SET `kode_golongan`='RBS',`nama_golongan`='MANAGER',`tunjangan_suami`='1000000,`tunjangan_anak`=400000,`uang_makan`=500000,`uang_lembur`=100000,`askes`=123321 WHERE kode_jabatan = 'BCA'")

# jabatan
cursor.execute("UPDATE `jabatan` SET `kode_jabatan`='BNI',`nama_jabatan`='Manager',`gapok`=3000000,`tunjangan_jabatan`=500000 WHERE kode_jabatan= 'BCA'")

# pegawai
cursor.execute("UPDATE `pegawai` SET `nip`=09129227,`nama_pegawai`='Raden Abel',`kode_jabatan`='MRI',`kode_golongan`='BCA',`status`='[value-5]',`jumlah_anak`='[value-6]' WHERE nip= 6512616217 ")
db.commit()

print("Data terupdate sudah :D")