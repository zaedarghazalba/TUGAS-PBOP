import csv
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

def menu_awal():
    while(True):
        print("        SELAMAT DATANG DI PERPUSTAKAAN MODERN YOGYAKARTA           ")
        print("------------------------------------------------------")
        print(" 1 Untuk Tampilkan Item")
        print(" 2 Untuk Pinjamkan Item")
        print(" 3 Untuk Kembalikan Item")  
        print(" 4 Untuk Tambahkan Item")
        print(" 5 Untuk Mencari Item")
        print(" 6 Untuk Keluar") 
        try:
            a=int(input("pilih menu 1-6: "))
            print()
            if(a==1):
                display_Item()
                kembali()
            elif(a==2):
                listSplit()
                pinjamkan_item()
                kembali()
            elif(a==3):
                listSplit()
                kembalikan_item()
                kembali()
            elif(a==4):
                listSplit()
                tambah_item()
                kembali()
            elif (a==5):
                cari_item()
            elif(a==6):
                print("Terimakasih telah menggunakan sistem perpustakaan kami")
                break
            else:
                print("Masukkan angka 1-5")
                kembali()
                continue
        except ValueError:
            print("masukkan sesuai petunjuk !")
            kembali()
            continue

def listSplit():
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
        with open("stockitem.txt","r+") as f:
        
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
def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

def display_Item():
    with open("stockitem.txt","r+") as f:
        lines=f.read()
        print(lines)
        print ()

def tambah_item():
        while(True):
                print("SILAHKAN PILIH KEY ITEM")
                print("1. BUKU")
                print("2. DVD")
                print("3. MAJALAH")  
                try:
                    b=int(input("pilih keyitem (TULIS DENGAN KAPITAL):"))
                
                    if(b==1):
                         b=("BUKU=")
                         with open("stockitem.txt", "a+") as f:
                                judul = input("judul = ")
                                isbn = input("ISBN =")
                                pengarang = input("pengarang =")
                                halaman = input("halaman = ")
                                ukuran = input ("ukuran buku =")
                                harga = input("harga denda = Rp ")   
                                pembatas = ","
                                f.write('\n'+ b + judul + pembatas + isbn + pembatas + pengarang + pembatas + halaman + ukuran + pembatas + 'Rp' + harga)
                    elif(b==2):
                         b=("DVD=")
                         with open("stockitem.txt", "a+") as f:
                                judul = input("judul = ")
                                pengarang = input("pengarang = ")
                                aktor = input("aktor = ")
                                genre =input("genrenya adalah =")
                                harga = input("harga denda = Rp ")   
                                pembatas = ","
                                f.write('\n'+ b + judul + pembatas + pengarang + pembatas + aktor + pembatas + genre + 'Rp' + harga)
                    elif(b==3):
                         b=("MAJALAH=")
                         with open("stockitem.txt", "a+") as f:
                                judul = input("judul = ")
                                pengarang = input("pengarang = ")
                                volume  = input("velume/halaman= ")
                                issue = input("issue =  ")   
                                harga = input("harga = Rp ")   
                                pembatas = ","
                                f.write('\n'+ b + judul + pembatas + pengarang + pembatas + volume + pembatas + issue + pembatas + 'Rp' + harga)
                except ValueError:
                        print("masukkan sesuai petunjuk   !")
                kembali()
                menu_awal()
def pinjamkan_item():
    success=False
    while(True):
        firstName=input("Masukkan nama depan peminjam: ")
        if firstName.isalpha():
            break
        print("Masukkan huruf A-Z")
    while(True):
        lastName=input("Masukkan nama belakang peminjam: ")
        if lastName.isalpha():
            break
        print("Masukkan huruf A-Z")
        print("")
    display_Item()
            
    t="Pinjaman-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               Perpustakaan Modern  \n")
        f.write("                   Dipinjam oleh: "+ firstName+" "+lastName+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N. \t\t Judul buku \t      Pengarang \n" )

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
                    with open("stockitem.txt","r+") as f:
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
                                with open("stockitem.txt","r+") as f:
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
                    pinjamkan_item()
                    success=False
                    continue
            except IndexError:
                print("")
                print("Pilih buku sesuai nomor.")
        except ValueError:
            print("")
            print("Pilih sesuai petunjuk !.")

def kembalikan_item():
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
        kembalikan_item()

    b="Pengembalian-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Perpustakaan Modern \n")
        f.write("                   Dikembalikan oleh: "+ name+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")


    total=0.0
    for i in range(8):
        if item[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+item[i]+"\t\tRp"+harga[i]+"\n")
                jumlah_stok[i]=int(jumlah_stok[i])+1
                with open("stockitem.txt","r+") as f:
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
    
        
    with open("stockitem.txt","r+") as f:
            for i in range(8):
                        f.write(item[i]+","+isbn[i]+","+pengarang[i]+","+str(jumlah_stok[i])+","+halaman[i]+","+ukuran[i]+","+"Rp"+harga[i]+"\n")
def cari_item():
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
                with open('stockitem.txt') as temp_f:
                        datafile = temp_f.readlines()
                        b=str(input("masukkan judul itemnya :"))
                        bukunya=a+b
                        print("ITEM YANG ANDA CARI ADALAH :",bukunya)
                for line in datafile:
                        if bukunya in line:
                                return True,print(line,"ITEM TERSEDIA") # The string is found
                return False,print("MAAF item YANG ANDA CARI TIDAK TERSEDIA")  # The string does not exist in the file
menu_awal()