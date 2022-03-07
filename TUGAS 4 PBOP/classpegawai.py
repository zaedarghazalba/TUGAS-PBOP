class pegawai :
        __nama = " "
        __alamat= " "
        __gaji= 0

        def __init__ (self,nama,alamat) :
             self.__nama =nama 
             self.__alamat=alamat
        def __hitunganGaji(self):
                upahLembur=20000
                gajiPokok = 2000000
                jumlhLembur=int(input("Total jam lembur :"))#raw_input
                self.__gaji=(upahLembur*jumlhLembur)+gajiPokok

        def tampilDetail(self):
                print("\n--Menghitung dan menampilkan detail gaji pegawai--")
                print("nama :",self.__nama )
                print("Alamat :",self.__alamat)
                self.__hitunganGaji()
                print("total gajiya adalah :",self.__gaji)

pegawai1=pegawai("Mikasa Ackerman","wall roseee")
pegawai1.tampilDetail()

pegawai2=pegawai("saya kisaragi ","prefektur naganooooo")
pegawai2.tampilDetail()