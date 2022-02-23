#tugas menghitung bangun ruang 2D atau 3D
#zaedar ghazalba
#5210411192


print("Berikut adalah luas dan keliling dari tabung ")
phi    = 22/7
jari   = float(input("Masukan Jari-jarinya  : "))
tinggi = float(input("Masukan Tinggginya    : "))
volume = phi*jari*jari*tinggi
luas   = 2*phi*jari*(jari+tinggi)

print("================HASILNYA ADALAH===================")
print("Volume Tabung         =","{:.2f}".format(volume))
print("Luas Permukaan Tabung =","{:.2f}".format(luas)) 
#tambahan penambahan "{:.2f}".format(), membatasi 2 karakter dibelakang koma.
#berikut hasil jika tidak pakai format dan tambahan 2f 
print("==========HASILNYA TANPA FORMAT===========")
print("Volume Tabung         =",(volume))
print("Luas Permukaan Tabung =",(luas)) 