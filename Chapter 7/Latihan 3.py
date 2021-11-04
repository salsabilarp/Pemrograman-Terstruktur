print('------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('------------------------------')

sum = 0
jumlah = 0

try:
    bil = int(input('Masukkan bilangan bulat : '))
    sum += bil
    jumlah += 1
    pilih = str(input('Lagi (y/n) : '))

    while pilih == 'y':
        bil = int(input('Masukkan bilangan bulat : '))
        sum += bil
        jumlah += 1
        pilih = str(input('Lagi (y/n) : '))

except ValueError:
    print('Bukan bilangan bulat')
    
    while pilih == 'y':
        bil = int(input('Masukkan bilangan bulat : '))
        sum += bil
        jumlah += 1
        pilih = str(input('Lagi (y/n) : '))

rata2 = sum/jumlah
print('Rata-ratanya adalah : ', rata2)

 


    

