buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rata2():
    print('Data buah :')
    for listbuah in buah:
        print('- {}'.format(listbuah), '( Harga Rp', buah[listbuah], ')')
    key = list(buah.keys())
    value = tuple(buah.values())
    ratarata = sum(value) / len(value)
    print('Rata-rata harga satuan dari keseluruhan buah yang ada adalah Rp ', ratarata)

rata2()
