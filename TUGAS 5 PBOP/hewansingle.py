#  SINGGLE INHERITENCE
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def suara(self):
        print('weawwwwwwwww...weawwwwwwwww...weawwwwwwwww')

k = Kucing()
k.suara()
k.bersuara()
