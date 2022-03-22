class Mahasiswa :
        def __init__ (self,nama,nim):
                self.nama=nama 
                self.nim=nim

        def detSiswa(self):
               print (self.nama,"alamat: wall roseeee")
                

class Siswa(Mahasiswa):
        def __init__ (self,nama,nim):
                self.nama= nama 
                self.nim = nim 

        def detSiswa(self):
                print(self.nama,"jurusan : informatika ")

mhs1=Siswa('naruto',2534859)
mhs2=Mahasiswa ('Nezuko',134252)

print(mhs1.nim,mhs1.nama)
mhs1.detSiswa()
print(mhs1.nim,mhs2.nama)
mhs2.detSiswa()
        