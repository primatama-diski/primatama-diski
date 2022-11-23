from texttable import Texttable
table = Texttable ()
jawab = 'y'
no = 'o'
nama = []
nim = []
ntugas = []
nuts = []
nuas = []

while (jawab == 'y'):
    nama.append (input('nama:'))
    nim.append (input('nim:'))
    ntugas.append (input('nilai tugas:'))
    nuas.append (input('nilai uas:'))
    nuts.append (input('nilai uts:'))
    jawab = input ('tambah data (y/t)?' )
    no = 1

print('             DAFTAR MAHASISWA        ')
for n in range (no):
    nt = float (ntugas[n])*30/100
    nu = float (nuts[n])*35/100
    na = float (nuas[n])*35/100
    akhir = nt+nu+na
    table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','Nilai Ahir'],
                    [n+1,nama[n],nim[n],ntugas[n],nuts[n],nuas[n],ahir]])
print(table.draw())