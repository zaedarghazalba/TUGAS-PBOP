#polymop dengan fungsi 
print(len("polymophism"))
print(len([0,1,2,3]))
'''
menggunakan fungsi len
output :
12 (tipe data str)
4 (tipe data list)
'''

#using class
class jerman :
        def ibukota(self):
                print("Berlin adalah ibukota jerman ")

class jepang :
        def ibukota(self):
                print("Tokyo adalah ibukota jepang")

negara1= jerman()
negara2 = jepang()
for country in (negara1,negara2):
        country.ibukota()