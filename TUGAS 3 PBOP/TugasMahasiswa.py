class Mahasiswa :
        def __init__(self,nama,nim,prodi,thn_masuk,jml_sks,hobi):
                self.nama = nama 
                self.nim = nim 
                self.prodi = prodi
                self.thn_masuk = thn_masuk 
                self.jml_sks = jml_sks
                self.hobi = hobi
m1 = Mahasiswa ('Udin','102012012','Sistem Informasi ',2020,22,'Badminton')
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m1.nama,m1.prodi,m1.thn_masuk,m1.nim,m1.jml_sks,m1.hobi)
print(teks)
m2 = Mahasiswa ( 'Asep','13123123','Informatika Medis',2021,24,'Renang')
teks1 = '{} adalah mahasiswa {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m2.nama,m2.prodi,m2.thn_masuk,m2.nim,m2.jml_sks,m2.hobi)
print(teks1)
m3 = Mahasiswa ('Doni','12234253','Informatika',2020,24,'Badminton dann renang')
teks2 = '{} adalah mahasiswa {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m3.nama,m3.prodi,m3.thn_masuk,m3.nim,m3.jml_sks,m3.hobi)
print(teks2)


            
