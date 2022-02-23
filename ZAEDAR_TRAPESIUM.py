#tugas menghitung bangun ruang 2D atau 3D
#zaedar ghazalba
#5210411192

def luas_trapesium () :
    print (' program mencari luas trapesium ')
    print ('--------------------------------------------')
    x= float (input('masukkan sisi atas trapesium : '))
    y= float(input('masukkan sisi bawah trapesium : '))
    z= float (input('masukkan tinggi trapesium : '))
    luas = (x+y)*z/2
    print ('')
    print("============HASILNYA=============")
    print ('luas trapesiumnya adalah : ' , luas, 'cm2')
luas_trapesium()