# membuka, membaca, dan menampilkan isi file

try:
    def file():
        namafile = str(input('Masukkan nama file : '))
        print('Isi file ', namafile, ' adalah :')
        tampilkan = open(namafile, "r")
        print(tampilkan.read())
    
    file()

except FileNotFoundError:
    print('File tidak ditemukan')
    
