teks = input('Ketikkan teks yang akan dienkripsi : ')
while True:
    try:
        n = int(input('Banyaknya pergeseran yang diinginkan : '))
        if n == True:
            True
        break
    except ValueError :
        print('Mohon hanya input bilangan bulat')


def enkripsi(teks, n):
    mylist = list(teks)
    
    for charact in range(len(mylist)) :
        if mylist[charact] != (' '):
            encrypt = (ord(mylist[charact]) + n)
            if encrypt > ord('Z'):
                encrypt -= 26
                mylist[charact] = chr(encrypt)
            elif encrypt < ord('Z'):
                mylist[charact] = chr(encrypt)

        else:
            continue
        
    tekshasil = ''.join(mylist)

    print ("Hasil enkripsi dari teks yang diinputkan adalah : ", tekshasil)

    # menulis hasil pada file baru
    buka = open('d:/hasilenkripsi.txt', 'w')
    buka.write(tekshasil)
    buka.close()

    return tekshasil

enkripsi(teks, n)
