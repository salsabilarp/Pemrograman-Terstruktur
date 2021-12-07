from datetime import *

file    = open('d:/datamember.txt', 'w')

pinjam  = datetime.date(datetime.now())
kembali = pinjam + timedelta(days=7)

while True:
    kode  = input('Masukkan Kode Member : ')
    nama  = input('Masukkan Nama Member : ')
    buku  = input('Masukkan Judul Buku  : ')
    ulang = input('Ulangi lagi (y/n)    : ')
    if ulang == 'y':
        file.write(kode + '|' + nama + '|' + buku + '|' + str(pinjam) + '|' + str(kembali) + '\n')
    elif ulang == 'n':
        file.write(kode + '|' + nama + '|' + buku + '|' + str(pinjam) + '|' + str(kembali) + '\n')
        file.close()
        break
    



