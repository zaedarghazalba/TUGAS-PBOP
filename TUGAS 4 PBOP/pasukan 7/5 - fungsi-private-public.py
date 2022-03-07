# fungsi private dan public

class Pegawai:
    __nama = ""
    __alamat = ""
    __gaji = 0

    def __init__(self, nama, alamat):
        self.nama=nama
        self.alamat=alamat

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

pegawai1=Pegawai("Mikasa Ackerman","wall roseee")
pegawai1.tampilDetail()

pegawai2=Pegawai("saya kisaragi ","prefektur nagano")
pegawai2.tampilDetail()