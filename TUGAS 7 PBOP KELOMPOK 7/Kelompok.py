class kalkulator :
        def __init__ (self,x,y):
                self.A = x
                self.B = y
                print ("A ="+str (x)+" Dan B = "+str(y))

        def tambah (self):
                self.hasil=self.A+self.B
                print ("A+B ="+str (self.hasil))

        def kurang (self) :
                self.hasil=self.A - self.B
                print ("A-B ="+str (self.hasil))

        def kali (self):
                self.hasil=self.A*self.B
                print("A x B ="+str (self.hasil))

        def pembagian (self):
                if self.B == 0:
                        print ("pembagian dengan 0")
                else:
                        self.hasil=self.A/self.B 
                        print("A/B ="+str (self.hasil))

        def anggota():
            kelompok = '''
ANGGOTA KELOMPOK

1. 5210411166_Naufal Firmansyah 
2. 5210411157_Raden Abel Zerach Jhonatan
3. 5210411167_Agnesta Lindasari
4. 5210411192_Zaedar Ghazalba

'''
            return print(kelompok)

while True :
    print('\nKALKULATOR KELOMPOK 7\n')

    print('1. Kalkulator')
    print('2. Anggota Kelompok')
    print('3. Exit')
    pilih = int(input('pilihan menu 1 - 3 : '))
    if pilih == 1 :

        inputan1 = int(input("\nMasukan Bilangan A   : "))

 
        print("\n=====INFORMATIKA=======")
        print('1. tambah')
        print('2. kurang')
        print('3. kali')
        print('4. bagi')

        pilih = int(input('\nPilihan Operator 1 - 5 : '))
        inputan2 = int(input("\nMasukan Bilangan B    : "))
        Object1 = kalkulator(inputan1,inputan2)
        if pilih == 1 :
            Object1.tambah()
            
        elif pilih == 2 :
            Object1.kurang()
        elif pilih == 3 :
            Object1.kali()
        elif pilih == 4 :
            Object1.pembagian()


    elif pilih == 2 :
        
        kalkulator.anggota()

    elif pilih == 3 :
        print(" Terimakasih Bu Endang Cantik ")
        break




