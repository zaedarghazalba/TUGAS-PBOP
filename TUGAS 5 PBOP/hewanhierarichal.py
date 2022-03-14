#  HIERACHICAL INHERITENCE 
class Induk:
    def fungsiinduk(self):
        print('fungsi pada parent class')

class anak1(Induk):
    def fungsianak1(self):
        print('fungsi pada anak 1')

class anak2(Induk):
    def fungsianak2(self):
        print('fungsi pada anak 2')

a1 = anak1()
a2 = anak2()

a1.fungsiinduk()
a1.fungsianak1()

a2.fungsiinduk()
a2.fungsianak2()
