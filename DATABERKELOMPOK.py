print('####################### STRING  ##########################')

str='aku cinta indonesia'
print(str)

str=str[:10]+'tanah air ku'+str[9:]
print(str)

str=''
print(str)
str1='aku cinta tanah air ku indonesia'
str1=str1 [:9]+''+str1[22:]
print(str1)

print('')
kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)
print('')

s='     python  '
s.strip()
print(s)
s.lstrip()
s.rstrip()
print('')

len(kelas)
jumlah=len (kelas)
print('panjang string adalah :',jumlah)
print('')

s1='python'
s2='programming'
print(s1+s2)
print('')

print(kelas)
print(kelas.index('a'))
print('')

kelas2=kelas.replace('praktikum','praktik')
print(kelas2)
print('')

a='satu'
b='dua'
c='tiga'
print('saya mempunyai %s mangga '%(b))
print('')

print(kelas2)
kelas2.split()

# input('hari ini adalah :')
# print('')

# data1=input('angka 1 :')
# data2=input('angka 2 :')
# hasil=int(data1)*int(data2)
# print(data1,'*',data2,'=',hasil)
# print('')
print('##################   LIST  #########################')
list=[0,1,2,3,4,5,6,7,8,9]
print(list)
print(list[0])
print(list[5])
print(list[:3])
print(len(list))
print(list[10-3:])
print(list[2:9])
print(list[-10])
print(list[0])
print('')

list.append(10)
print(list)
list2=['hallo']
list.extend(list2)
print(list2)
print(list)
list.extend('hai')
print(list)
del list[1]
print(list)
list.remove(10)
print(list)
print(list.pop())
print(list.pop(2))
print(list)
print('')

a=[50,10,20,30,40]
b=sorted(a)
print(b)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print('')

print(min(a))
print(max(a))
print('###################  DICTIONARY  #######################')

d={1:100,2:200,3:300,4:400,5:500}
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[1]
print(d)
print('')
e=d.copy()
print(e)
d.clear()
print(d)
print(len(d))
print('##################  TUPLE  ########################')


t=(100,200,300,400,500)
print(t)
print(t[0])
print(t[3])
print(t.index(200))
t2=(10,20,30,40,50,60)
print(t.count(20))
print(t2.count(10))

print('###################### SET  ####################')


exmpl = [10,20,30,40]
exmpl2 = [60,70,80,90,100]

set = set(exmpl) # conver list menjadi set
print('menggunakan add ;')
print('sebelum ditambah (add) :',set)
set.add(50) # menambah element kedalam set  
print('setelah ditambahkan (add) :',set) 
print('')

# update set
set.update( exmpl2 )
print('setelah di update dengan list 2')
print(set)
print('')

# delete set dengan discard
set.discard(10)
print('menghapus element 10 didalam set :')
print(set)
print('')

#delete set dengan menggunakan remove 
set.remove(100)
print('menghapus dengan menentukan nilai mana yang akan dihapus :')
print('setelah dilakukan remove angka 100 maka hasil akan :',set)
print('')

#menghapus dengan pop (indek random)
set.pop()
print('menghapus data random :')
print('maka hasil akan seperti ini :',set)
print('')

#jika ingin menghapus semua maka menggunkan clear
set.clear()
print('menghapus semua data :')
print('hasil setelah di clear atau hapus semua data  :',set)
print('')

set2 = {1000,2000,3000,4000,5000}

#copy set ke dalam variable lain
print('mengcopy set 2 menuju set 3')
set3 = set2.copy()
print('setelah di copy maka nilai akan tercopy :',set2)
print('')


set1={100,200,300,400,500}
set4={11,22,33,44,55,66,77}
print('kita akan mencoba menggabungkan set set menjadi satu set')
print('dimana jika ada index yang sama maka akan diambil salah satu aja')
print('tetapi hasil dari setnya tidak akan urut ')
set5=set2.union(set3,set4)
print(set5)










