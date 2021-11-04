# membuka, membaca, dan menampilkan isi file

def file():
    namafile = str(input('Masukkan nama file : '))
    print('Isi file ', namafile, ' adalah :')
    tampilkan = open(namafile, "r")
    print(tampilkan.read())
    
file()
    
