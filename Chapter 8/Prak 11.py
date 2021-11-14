buah = {'apel': 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}


print('Data buah :')
for listbuah in buah:
    print('- {}'.format(listbuah), '( Harga Rp', buah[listbuah], ')')
    
print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')


while True:
    try:
        pilihan = str(input('Pilihan anda : '))
        if(pilihan == 'A' or pilihan == 'a'):
            while True:
                tambah = str(input('Silahkan menambahkan data buah : '))
                if(tambah in buah):
                    print('upss.. nama buah sudah ada dalam dictionary')
                    continue
                elif(tambah not in buah):
                    harga = int(input('Silahkan masukkan harga satuan : '))
                    buah[tambah] = harga
                    lagi = str(input('Tambah lagi (y/n)? :'))
                    if lagi == 'y':
                        continue
                    elif lagi == 'n':
                        print('Data Buah : ')
                        for listbuah in buah:
                            print('- {}'.format(listbuah),
                                  '( Harga Rp', buah[listbuah], ')')
                break

    
        elif(pilihan == 'B' or pilihan == 'b'):
            sum = 0
            while True:
                 nama = str(input('Nama buah yang dibeli : '))
                 banyak = float(input('Berapa Kg             : '))
                 if nama in buah:
                    harga = int(buah[nama])
                    bayar = harga * banyak
                    sum += bayar
                    lagi = str(input('Beli buah yang lain (y/n)? :'))
                    if lagi == 'y':
                        True
                    elif lagi == 'n':
                        print('=' * 30)
                        print('Total harga           :', sum)
                        break
        else:
            print('Pilihan tidak tersedia')
        
    except KeyError:
        print('Buah tidak tersedia')
    except ValueError:
        print('input tidak valid')
