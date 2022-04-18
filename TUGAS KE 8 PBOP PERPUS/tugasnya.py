import csv
import os
import sys
class PerpusItem :
        def __init__(self,judul,subjek,lokasi,info,stock):
                self.judul = judul
                self.subjek = subjek
                self.lokasi = lokasi
                self.info = info
                self.jumlah_stock = stock
        def display_Item(self):
            with open("stock.txt","r+") as f:
                lines=f.read()
                print(lines)
                print ()
        def clear_screen(self):
                os.system('cls' if os.name == 'nt' else 'clear')

        def kembali(self):
                print("\n")
                input("Tekan tombol apa saja untuk kembali...")

        def tambah_item(self):
                  while(True):
                         print("SILAHKAN PILIH KEY ITEM")
                         print("1. BUKU")
                         print("2. DVD")
                         print("3. MAJALAH")  
                         menu=int(input("pilih menu:"))    
                         if(menu==1): 
                            menu=("BUKU=")        
                            with open("stock.txt", "a+") as f:
                                        judul = input("judul = ")
                                        isbn = input("ISBN =")
                                        pengarang = input("pengarang =")
                                        jumlah_stok = input(" jumlah stock buku :")
                                        halaman = input("halaman = ")
                                        ukuran = input ("ukuran buku =")                                          
                                        pembatas = ","
                                        harga = input("harga pinjam :")
                                        f.write('\n'+ menu + judul + pembatas + isbn + pembatas + pengarang + pembatas +jumlah_stok+ pembatas+ halaman + ukuran + pembatas + 'Rp' + harga)
                                        print("DATA BERHASIL DITAMBAHKAN")
                                        library.kembali('self')
                                        break
                         elif(menu==2):
                                menu=("DVD=")
                                with open("stock.txt", "a+") as f:
                                        judul = input("judul = ")
                                        pengarang = input("pengarang = ")
                                        aktor = input("aktor = ")
                                        genre =input("genrenya adalah =")
                                        jumlah_stok = input("jumlah stok :")
                                        pembatas = ","
                                        harga = input("harga pinjam :")
                                        f.write('\n'+ menu + judul + pembatas + pengarang + pembatas + aktor + pembatas + jumlah_stok + pembatas + genre + pembatas+ 'Rp' + harga)
                                        print("DATA BERHASIL DITAMBAHKAN")
                                        library.kembali('self')
                                        break
                         elif(menu==3):
                                menu=("MAJALAH=")
                                with open("stock.txt", "a+") as f:
                                        judul = input("judul = ")
                                        pengarang = input("pengarang = ")
                                        volume  = input("velume/halaman= ")
                                        issue = input("issue =  ")                                            
                                        pembatas = ","
                                        jumlah_stok = input("jumlah stock :")
                                        harga = input("harga pinjam :")
                                        f.write('\n'+ menu + judul + pembatas + pengarang + pembatas + volume + pembatas + issue + jumlah_stok+ pembatas+ 'Rp' + harga  )
                                        print("DATA BERHASIL DITAMBAHKAN")
                                        library.kembali('self')
                                        break
                         else:
                                print("masukkan sesuai petunjuk   !")
                
class Buku (PerpusItem) : 
        def __init__ (self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran):
                super().__init__ (judul,'Buku',lokasi,info)
                self.isbn = isbn
                self.pengarang = pengarang 
                self.jmlhal = jmlhal
                self.ukuran = ukuran

class Majalah (PerpusItem):
        def __init__ (self,judul,subjek,lokasi,info,volume,issue):
                super().__init__(judul,'Majalah',lokasi,info)
                self.volume = volume
                self. issue = issue

class DVD (PerpusItem):
        def __init__(self,judul,subjek,lokasi,info,aktor,genre):
                super().__init__(judul,'DVD',lokasi,info)
                self.aktor = aktor
                self. genre = genre

class Katalog(PerpusItem):
        def __init__(self,cari,judul,subjek,lokasi,info):
                self.cari=cari
                self.judul = judul
                self.subjek = subjek
                self.lokasi = lokasi
                self.info = info
        
        def cari_item(self):
          while(True):
                print("SILAHKAN PILIH KEY ITEM")
                print("1. BUKU")
                print("2. DVD")
                print("3. MAJALAH")  
                try:
                    a=int(input("pilih keyitem :"))
                    if(a==1):
                         a=("BUKU=")
                    elif(a==2):
                         a=("DVD=")
                    elif(a==3):
                         a=("MAJALAH=")
                    else:
                         continue
                except ValueError:
                        print("masukkan sesuai petunjuk   !")
                with open('stock.txt') as temp_f:
                        datafile = temp_f.readlines()
                        b=str(input("masukkan judul itemnya :"))
                        bukunya=a+b
                        print("ITEM YANG ANDA CARI ADALAH :",bukunya)
                for line in datafile:
                        if bukunya in line:
                                return True,print(line,"ITEM TERSEDIA") # The string is found
                return False,print("MAAF item YANG ANDA CARI TIDAK TERSEDIA")  # The string does not exist in the file
class borrow(PerpusItem):
        def __init__(self,judul,subjek,lokasi,info):
                self.judul = judul
                self.subjek = subjek
                self.lokasi = lokasi
                self.info = info
        def listSplit(self):
            global item
            global pengarang
            global jumlah_stok
            global harga
            global isbn
            global halaman
            global ukuran
            global aktor
            global genre
            global volume
            global issue
            item = []
            isbn=[]
            halaman=[]
            ukuran=[]
            pengarang=[]
            jumlah_stok=[]
            harga=[]
            aktor=[]
            genre=[]
            volume=[]
            issue=[]
            with open("stock.txt","r+") as f:
        
                lines=f.readlines()
                lines=[x.strip('\n') for x in lines]
                for i in range(len(lines)):
                    ind=0
                    for a in lines[i].split(','):
                        if(ind==0):
                            item.append(a)
                        elif(ind==1):
                              isbn.append(a)
                        elif(ind==2):
                              pengarang.append(a)
                        elif(ind==3):
                              jumlah_stok.append(a)
                        elif(ind==4):
                             halaman.append(a)
                        elif(ind==5):
                             ukuran.append(a)
                        elif(ind==6):
                             harga.append(a.strip("Rp"))
                        elif(ind==7):
                             aktor.append(a)
                        elif(ind==8):
                             genre.append(a)
                        elif(ind==9):
                             volume.append(a)
                        elif(ind==10):
                             issue.append(a)
                        ind+=1
        def getDate(self):
                import datetime
                now=datetime.datetime.now
                return str(now().date())

        def getTime(self):
                import datetime
                now=datetime.datetime.now
                return str(now().time())
        def pinjamkan_item(self):
            success=False
            while(True):
                 print("PENGUMUMAN")
                 print("MOHON UNTUK MEMPERHATIKAN,FITUR PINJAM ITEM HANYA UNTUK BUKU,\nDVD DAN MAJALAH MASIH DALAM PENGEMBANGAN\nTERIMAKASIH ATAS PERHATIANNYA ")
                 print("Masukkan huruf A-Z")   
                 firstName=input("Masukkan nama depan peminjam: ")
                 if firstName.isalpha():
                     break
            while(True):
                 lastName=input("Masukkan nama belakang peminjam: ")
                 if lastName.isalpha():
                     break
                 print("  ")
                 print("     ")
            with open("stock.txt","r+") as f:
                lines=f.read()
                print(lines)
                print ()   
                t="Pinjaman-"+firstName+".txt"
                with open(t,"w+") as f:
                      f.write("               Perpustakaan Modern  \n")
                      f.write("                   Dipinjam oleh: "+ firstName+" "+lastName+"\n")
                      f.write("    Tanggal: " +pinjamitem.getDate('self')+"    Waktu:"+pinjamitem.getTime('self')+"\n\n")
                      f.write("S.N. \t\t Judul buku \t  isbn \n" )

                while success==False:
                      print("Pilih menu di bawah ini :")
                      for i in range(len(item)):
                          print("Masukkan", i, "untuk meminjam buku", item[i])                   
                      try:   
                          a=int(input())
                          try:
                              if(int(jumlah_stok[a])>0):
                                  print("Buku Tersedia")
                                  with open(t,"a") as f:
                                      f.write("1. \t\t"+ item[a]+"\t\t  "+isbn[a]+"\n")
                                  jumlah_stok[a]=int(jumlah_stok[a])-1
                                  with open("stock.txt","r+") as f:
                                      for i in range(8):
                                          f.write(item[i]+","+isbn[i]+","+pengarang[i]+","+str(jumlah_stok[i])+","+halaman[i]+","+ukuran[i]+","+"Rp"+harga[i]+"\n")
                                          continue
                                  #jika buku yang dipinjam lebih dari 1
                                  loop=True
                                  count=1
                                  while loop==True:
                                      choice=str(input("Apakah ingin pinjam buku lagi ? Masukkan Y jika ya dan N jika tidak."))
                                      if(choice.upper()=="Y"):
                                           count=count+1
                                           print("Pilih menu di bawah ini :")
                                           for i in range(len(item)):
                                               print("Masukkan", i, "untuk meminjam buku", item[i]) 
                                           a=int(input())
                                           if(int(jumlah_stok[a])>0):
                                                print("Buku tersedia")
                                                with open(t,"a") as f:
                                                    f.write(str(count) +". \t\t"+ item[a]+"\t\t  "+isbn[a]+"\n")

                                                jumlah_stok[a]=int(jumlah_stok[a])-1
                                                with open("stock.txt","r+") as f:
                                                    for i in range(8):
                                                        f.write(item[i]+","+isbn[i]+","+pengarang[i]+","+str(jumlah_stok[i])+","+halaman[i]+","+ukuran[i]+","+"Rp"+harga[i]+"\n")
                                                        success=False
                                                        continue
                                           else:
                                               loop=False
                                               continue
                                      elif (choice.upper()=="N"):
                                          print ("Terimakasih telah meminjam buku. ")
                                          print("")
                                          loop=False
                                          success=True
                                      else:
                                           print("Masukkan sesuai petunjuk !")

                              else:
                                  print("Buku tidak tersedia")
                                  pinjamitem.pinjamkan_item('self')
                                  success=False
                                  continue
                          except IndexError:
                               print("")
                               print("Pilih buku sesuai nomor.") 
                      except ValueError:
                           print("")
                           print("Pilih sesuai petunjuk !.") 
class giveback(PerpusItem):
        def __init__(self,judul,subjek,lokasi,info):
                self.judul = judul
                self.subjek = subjek
                self.lokasi = lokasi
                self.info = info
        def kembalikan_item(self):
                name=input("Masukkan nama peminjam: ")
                a="Pinjaman-"+name+".txt"
                try:
                    with open(a,"r") as f:
                        lines=f.readlines()
                        lines=[a.strip("Rp") for a in lines]
                
                    with open(a,"r") as f:
                        data=f.read()
                        print(data)
                except:
                      print("Nama peminjam salah")
                      balikin.kembalikan_item()
                b="Pengembalian-"+name+".txt"
                with open(b,"w+")as f:
                        f.write("                Perpustakaan Modern \n")
                        f.write("                   Dikembalikan oleh: "+ name+"\n")
                        f.write("    Tanggal: " +pinjamitem.getDate('self')+"    Waktu:"+pinjamitem.getTime('self')+"\n\n")
                        f.write("S.N.\t\tJudul Buku\t\tTotal\n")
                total=0.0
                for i in range(8):
                        if item[i] in data:
                           with open(b,"a") as f:
                                f.write(str(i+1)+"\t\t"+item[i]+"\t\tRp"+harga[i]+"\n")
                                jumlah_stok[i]=int(jumlah_stok[i])+1
                                with open("stock.txt","r+") as f:
                                      for i in range(8):
                                          f.write(item[i]+","+isbn[i]+","+pengarang[i]+","+str(jumlah_stok[i])+","+halaman[i]+","+ukuran[i]+","+"Rp"+harga[i]+"\n")
                           total+=float(harga[i])
                print("\t\t\t\t\t\t\t"+"Rp"+str(total))
                print("Apakah buku melewati batas peminjaman?")
                print("Masukkan Y jika ya dan N jika tidak")
                stat=input()
                if(stat.upper()=="Y"):
                        print("Berapa hari keterlambatan?")
                        hari=int(input())
                        denda=3000*hari
                        with open(b,"a+")as f:
                            f.write("\t\t\t\t\tDenda: Rp"+ str(denda)+"\n")
                        total=total+denda
                print("Total pembayaran: "+ "Rp"+str(total))
                with open(b,"a")as f:
                    f.write("\t\t\t\t\tTotal: Rp"+ str(total))
                
                        
                # with open("stock.txt","r+") as f:
                #         for i in range(8):
                #                     f.write(item[i]+","+isbn[i]+","+pengarang[i]+","+str(jumlah_stok[i])+","+halaman[i]+","+ukuran[i]+"\n")


if __name__ == "__main__":
    katalog=Katalog    
    library=PerpusItem
    pinjamitem=borrow
    balikin=giveback
    while(True):
        print("        SELAMAT DATANG DI PERPUSTAKAAN MODERN YOGYAKARTA           ")
        print("------------------------------------------------------")
        print(" 1 Untuk Tampilkan Item")
        print(" 2 Untuk Pinjamkan Item")  
        print(" 3 Untuk Tambahkan Item")
        print(" 4 untuk kembalikan item")
        print(" 5 Untuk Mencari Item")
        print(" 6 Untuk Keluar") 
        try:  
            a=int(input("pilih menu 1-6: "))
            print()
            if(a==1):
                library.display_Item('self')
            elif (a==2):
                    pinjamitem.listSplit('self')
                    pinjamitem.pinjamkan_item('self')
                    library.kembali('self')
            elif (a==3):
                    library.tambah_item('self')
                    library.kembali('self')   
            elif (a==4):
                    pinjamitem.listSplit('self')
                    balikin.kembalikan_item('self')
                    library.kembali('self')  
            elif (a==5):
                   katalog.cari_item('self')
                   library.kembali('self')
            elif (a==6):
                    print("terimakasih sudah menggunakan layanan kami")
                    break 
                    
            else:
                library.kembali('self')
                continue
        except ValueError:
            print("masukkan sesuai petunjuk !")
            library.kembali()
            continue