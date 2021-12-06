file = open('d:/listdata.txt', 'w')
while True:
    NIM = str(input('Masukkan NIM       : '))
    nama = str(input('Masukkan Nama Mhs  : '))
    alamat = str(input('Masukkan Alamat    : '))
    ulang = str(input('Ulangi input lagi (y/n) : '))
    if ulang == 'y':
        file.write(NIM + '|' + nama + '|' + alamat + '\n' )
    elif ulang == 'n':
        file.write(NIM + '|' + nama + '|' + alamat + '\n' )
        file = open('d:/listdata.txt', 'r')
        read = file.read()
        file.close()
        print('===========================',
              '\nData Mahasiswa : ')
        print(read)
        break


