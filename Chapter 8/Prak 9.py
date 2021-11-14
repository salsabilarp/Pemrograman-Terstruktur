buah = {'apel': 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}
print('Data buah :')
for listbuah in buah:
    print('- {}'.format(listbuah),
          '( Harga Rp', buah[listbuah], ')')

while True:
    nama = str(input('Nama buah yang dibeli : '))
    banyak = int(input('Berapa Kg             : '))
    if nama in buah:
        bayar = banyak * buah[nama]
        print('=' * 30)
        print('Total harga           :', bayar)
        break
    else:
        print('Buah tidak tersedia')
