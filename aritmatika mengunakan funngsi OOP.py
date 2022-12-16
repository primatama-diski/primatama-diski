class OperasiAritmatika:
    # -- deklarasi property:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    # -- Operasi Aritmatika Dasar:
    def Bilangan1(self):
        return self.X

    def Bilangan2(self):
        return self.Y

    def tambah(self):
        return self.X + self.Y

    def kurang(self):
        return self.X - self.Y

    def kali(self):
        return self.X * self.Y

    def bagi(self):
        return self.X / self.Y

    def sisa(self):
        return self.X % self.Y


# -- program utama & pemanggilan
op = OperasiAritmatika(8,10)
bil1 = op.Bilangan1()
bil2 = op.Bilangan2()
opTambah = op.tambah()
opKurang = op.kurang()
opKali = op.kali()
opBagi = op.bagi()
opSisa = op.sisa()
print('-- Operasi Aritmatika Sederhana --')
print('   ..Dengan OOP Bahasa python..')
print('==================================')
print('Bilangan Kesatu(X)        = ', bil1)
print('Bilangan Kesatu(Y)        = ', bil2)
print('Penjumlahan 2 Bilangan    = ', opTambah)
print('Pengurangan 2 Bilangan    = ', opKurang)
print('Perkalian 2 Bilangan      = ', opKali)
print('Pembagian 2 Bilangan      = ', opBagi)
print('Sisa Pembagian 2 Bilangan = ', opSisa)
print('==================================')