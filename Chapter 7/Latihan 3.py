print('------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('------------------------------')

sum = 0
jumlah = 0
while True :
    try:
        bil = int(input('Masukkan bilangan bulat : '))
        sum += bil
        jumlah += 1
        pilih = str(input('Lagi (y/n) : '))

        if(pilih == 'y'):
            True
        elif(pilih == 'n'):
            False
            break
        else:
            print('Input tidak valid')
            break
    except ValueError:
        print('Bukan bilangan bulat')
        continue
    
rata2 = sum/jumlah
print('Rata-ratanya adalah : ', rata2)

 


    

