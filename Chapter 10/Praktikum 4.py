# membuka file
file = open('d:/listdata.txt', 'r')
read = file.readlines()

# input data
cari = input('Masukkan NIM yang mau dicari : ')

# menampilkan data
for listdata in range(len(read)):
    if cari in read[listdata]:
        split = read[listdata].split('|')
        print(('=' * 39) + '\n' +
              'Hasil pencarian data mahasiswa \n' +
              'NIM    : ' + split[0] + '\n' +
              'Nama   : ' + split[1] + '\n' +
              'Alamat : ' + split[2] + '\n')
        break

if cari not in read[listdata]:
    print('Data mahasiswa tidak ditemukan')

#menutup file
file.close()

