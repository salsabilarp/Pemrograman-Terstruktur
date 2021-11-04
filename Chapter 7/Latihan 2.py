# membuka dan menambahkan data ke dalam file

try:
    namafile = str(input('Masukkan nama file : '))
    tambahdata = str(input('Data yang mau ditambahkan : '))
    tambahdata2 = str(input('Mau lagi (y/n) : '))
    while tambahdata2 == 'y':
        tambahdataa =(str(input('Data yang mau ditambahkan : ')))
        tambahdata += tambahdataa
        tambahdata2 = str(input('Mau lagi (y/n) : '))

    files = open(namafile, 'a')
    files.write('\n' + tambahdata)
    files.close()

    files = open(namafile, 'r')
    print(files.read())
    
except FileNotFoundError:
    print('File tidak ditemukan')


        
    

