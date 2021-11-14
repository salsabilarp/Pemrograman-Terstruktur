datasayur = {'bayam', 'kangkung', 'wortel', 'selada'}
print('Data sayur :')
for list in datasayur:
    print('-', list)

print('Menu :')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')

while True:
    pilihan = str(input('Pilihan anda : '))
    if(pilihan == 'A' or pilihan == 'a'):
        while True:
            tambah = str(input('Silahkan menambahkan data sayur : '))
            if tambah in datasayur:
                print('Data sayur sudah ada')
            else:
                datasayur.add(tambah)
                lagi = str(input('Tambah lagi (y/n)? :'))
                if lagi == 'y':
                    continue
                elif lagi == 'n':
                    break
                
    elif(pilihan == 'B' or pilihan == 'b'):
        while True:
            hapus = str(input('Data sayur yang akan dihapus : '))
            if hapus in datasayur:
                datasayur.remove(hapus)
                lagi = str(input('Hapus lagi (y/n)? :'))
                if lagi == 'y':
                     continue
                elif lagi == 'n':
                    break
            else:
                print('Maaf data tidak ditemukan')
            
    elif(pilihan == 'C' or pilihan == 'c'):
        print('Data sayur terbaru :')
        for sayor in datasayur:
            print('-', sayor)
        break
    else:
        print('Input tidak valid')

