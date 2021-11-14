buah = {'apel': 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}
print('Data buah :')
for listbuah in buah:
    print('- {}'.format(listbuah),
          '( Harga Rp', buah[listbuah], ')')

sum = 0
while True:
    try:
        nama = str(input('Nama buah yang dibeli : '))
        banyak = int(input('Berapa Kg             : '))
        bayar = banyak * buah[nama]
        sum += bayar
        lagi = str(input('Beli buah yang lain (y/n)? :'))
        if lagi == 'y':
            True
        elif lagi == 'n':
            print('=' * 30)
            print('Total harga           :', sum)
            break
        
    except KeyError:
        print('Buah tidak tersedia')
    except ValueError:
        print('input tidak valid')
