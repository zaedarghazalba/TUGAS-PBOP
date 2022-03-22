class Mahasiswa:
        def __init__ (self,nama,nim):
                self.nama =nama 
                self.nim = nim
                #self.prodi = prodi
                #self.thn_msk = thn_msk
                #self.semester = semester

        def SyaratSkripsi (self,totalsks):
                if totalsks >= 100 :
                        print (f"selamat {self.nama},anda memenuhi syarat untuk mengambil skripsi")
                else:
                        print(f"mohon maaf {self.nama} ,anda belum memenuhi syarat untuk mengambil skripsi")

        def tampilMhs(self):
                print ("nama :" ,self.nama,",nim :",self.nim)

                #methode overloading
        def hitungSKS(self,jmlsks=None,sks=None):
                if jmlsks !=None and sks!=None :
                        totalsks = jmlsks+sks
                        print("total sks : ",totalsks)
                        self.SyaratSkripsi(totalsks)
                else:
                        totalsks = jmlsks
                        print("Total sks :",totalsks)
                        self.SyaratSkripsi(totalsks)
        
#memanggil kelas
mhs1= Mahasiswa("eren seger",123456)
mhs2 = Mahasiswa("lupppy",56382638628)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80,34)#overloading
mhs2.hitungSKS(83)#overloading