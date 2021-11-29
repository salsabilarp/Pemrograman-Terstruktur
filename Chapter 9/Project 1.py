def ubahHuruf(teks, a, b):
    mylist = list(teks)
    ubah = teks.replace(a, b)
    gabung = ' '.join([ubah])
    print(gabung)

ubahHuruf('MATEMATIKA', 'T', 'S')
 
