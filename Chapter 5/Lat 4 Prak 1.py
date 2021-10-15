#latihan 4 Praktikum 1
import math
kodekaryawan = int(input('Masukkan kode karyawan : '))
namakaryawan = input('Masukkan nama karyawan : ')
golongan = input('Masukkan golongan : ')

print('=======================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('---------------------------------------')

print('Nama Karyawan     : ' + namakaryawan + ' ' + 'Kode : ' + str(kodekaryawan))
print('Golongan          : ' + str(golongan))

print('---------------------------------------')

if(golongan == 'A'):
    Gajipokok = 10000000
    Potongan = 2.5 
    BesarPotongan = Gajipokok * (Potongan / 100)
    Gajibersih = Gajipokok - round(BesarPotongan)

elif(golongan == 'B'):
    Gajipokok = 8500000
    Potongan = 2.0
    BesarPotongan = Gajipokok * (Potongan / 100)
    Gajibersih = Gajipokok - round(BesarPotongan)
    
elif(golongan == 'C'):
    Gajipokok = 7000000
    Potongan = 1.5
    BesarPotongan = Gajipokok * (Potongan / 100)
    Gajibersih = Gajipokok - round(BesarPotongan)
    
elif(golongan == 'D'):
    Gajipokok = 5000000
    Potongan = 1.0
    BesarPotongan = Gajipokok * (Potongan / 100)
    Gajibersih = Gajipokok - round(BesarPotongan)
    
print('Gaji Pokok        : Rp ' + str(Gajipokok))
print('Potongan' + '(' + str(Potongan)  + '%)' + '    : Rp ' +  str(BesarPotongan))
print('------------------------------------- -')
print('Gaji Bersih       : Rp ' + str(Gajibersih))
