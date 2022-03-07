class Mahasiswa :
        def __init__(self,nama,nim,prodi,thn_masuk,jml_sks,hobi,umur):
                self.nama = nama 
                self.nim = nim 
                self.prodi = prodi
                self.thn_masuk = thn_masuk 
                self.jml_sks = jml_sks
                self.hobi = hobi
                self.Mahasiswa__umur = umur 
m1 = Mahasiswa ('Udin','102012012','Sistem Informasi ',2020,22,'Badminton',22)
teks = '{} adalah mahasiswa dengan umur {} dan masuk ke prodi {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m1.nama,m1.Mahasiswa__umur,m1.prodi,m1.thn_masuk,m1.nim,m1.jml_sks,m1.hobi)
print(teks)
m2 = Mahasiswa ( 'Asep','13123123','Informatika Medis',2021,24,'Renang',24)
teks1 = '{} adalah mahasiswa dengan umur {} dan masuk ke prodi {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m2.nama,m2.Mahasiswa__umur,m2.prodi,m2.thn_masuk,m2.nim,m2.jml_sks,m2.hobi)
print(teks1)
m3 = Mahasiswa ('Doni','12234253','Informatika',2020,24,'Badminton dann renang',23)
teks2 = '{} adalah mahasiswa dengan umur {} dan masuk ke prodi {} angkatan {} dengan nim {} jumlah sks {} dan mempunyai hobi {}'.format (m3.nama,m3.Mahasiswa__umur,m3.prodi,m3.thn_masuk,m3.nim,m3.jml_sks,m3.hobi)
print(teks2)

#saya menambahkan atribut private umur pada objek m1,m2 dan m3 pada class mahasiswa


            