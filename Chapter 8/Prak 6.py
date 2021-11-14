myData = []

def sortStringByChar():
    while True:
        nama = str(input('Masukkan data buah : '))
        myData.append(nama)
        
        while True:
            tambah = str(input('lagi (y/n)? : '))
            if(tambah == 'y'):
                nama = str(input('Masukkan data buah : '))
                myData.append(nama)
            elif(tambah == 'n'):
                print('List data buah : ', myData)
                break
            else:   
                print('Input tidak valid')
                continue

        myData.sort(key = len, reverse = True)
        print('Urutan list data berdasarkan jumlah karakter : ', myData)
        break
    
sortStringByChar()
