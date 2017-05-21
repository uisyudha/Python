class Mobil(object):
    posisi = 0
    kecepatan = 10

    def __init__(self, posisiAwal):
        self.posisi = self.posisi + posisiAwal

    def maju(self):
        self.posisi = self.posisi + self.kecepatan

    def getPosisi(self):
        return self.posisi


mobilBaru = Mobil(2)
print mobilBaru.getPosisi()
print mobilBaru.maju()
print mobilBaru.getPosisi()
