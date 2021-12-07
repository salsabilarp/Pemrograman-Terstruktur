from datetime import *

def diffDate(x):
    split  = x.split('-')
    tahun  = int(split[0])
    bulan  = int(split[1])
    hari   = int(split[2])
    tgl = date(tahun, bulan, hari)
    today  = datetime.date(datetime.now())
    selisih = tgl - today
    hasil = selisih.days

    return(hasil)

file = open('d:/datamember.txt', 'r')
read = file.readlines()

kode = input('Masukkan Kode Member : ')

for listdata in range(len(read)):
    if kode in read[listdata]:
        y = read[listdata].split('|')
        kembali = datetime.date(datetime.now())
        terlambat = diffDate(y[4])
        denda = int(terlambat) * 2000
        print('\n' +
              'Data Peminjaman Buku \n' +
              'Kode Member                 : ' + y[0] + '\n' +
              'Nama Member                 : ' + y[1] + '\n' +
              'Judul Buku                  : ' + y[2] + '\n' +
              'Tanggal Mulai Peminjaman    : ' + y[3] + '\n' +
              'Tanggal Maksimal Peminjaman : ' + y[4] +
              'Tanggal Pengembalian        : ' + str(kembali) + '\n' +
              'Terlambat                   : ' + str(terlambat) + ' hari' + '\n' +
              'Denda                       : ' + 'Rp ' + str(denda))

        break

if kode not in read[listdata]:
    print('Data member tidak ditemukan')

#menutup file
file.close()
