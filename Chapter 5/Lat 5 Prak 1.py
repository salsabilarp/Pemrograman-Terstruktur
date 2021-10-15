#latihan 4 Praktikum 1

kodekaryawan = int(input('Masukkan kode karyawan : '))
namakaryawan = input('Masukkan nama karyawan : ')
golongan = input('Masukkan golongan : ')
status = input('Masukkan status (1:menikah, 2:blm) : ')

if status == '1':
    print('Masukkan jumlah anak ')
    jumlahanak = int(input(':'))
else:
    jumlahanak = 0
    tunjanganIS = 0
    tunjanganA = 0

print('=======================================')
print('STRUK RINCIAN GAJI KARYAWAN')

print('---------------------------------------')

print('Nama Karyawan             : ' + namakaryawan + ' ' + 'Kode : ' + str(kodekaryawan))
print('Golongan                  : ' + str(golongan))
print('Status Menikah            : ' + str(status))
print('Jumlah Anak               : ' + str(jumlahanak))

print('---------------------------------------')

if(golongan == 'A'):
    Gajipokok = 10000000
    Potongan = 2.5 
    BesarPotongan = Gajipokok * (Potongan / 100)
    tunjanganIS = 10 / 100 * Gajipokok
    tunjanganA = 5 /100 * Gajipokok * jumlahanak
    Gajikotor = Gajipokok + round(tunjanganIS) + round(tunjanganA)
    Gajibersih = Gajikotor - round(BesarPotongan)

elif(golongan == 'B'):
    Gajipokok = 8500000
    Potongan = 2.0
    BesarPotongan = Gajipokok * (Potongan / 100)
    tunjanganIS = 10 / 100 * Gajipokok
    tunjanganA = 5 /100 * Gajipokok * jumlahanak
    Gajikotor = Gajipokok + round(tunjanganIS) + round(tunjanganA)
    Gajibersih = Gajikotor - round(BesarPotongan)
    
elif(golongan == 'C'):
    Gajipokok = 7000000
    Potongan = 1.5
    BesarPotongan = Gajipokok * (Potongan / 100)
    tunjanganIS = 10 / 100 * Gajipokok
    tunjanganA = 5 /100 * Gajipokok * jumlahanak
    Gajikotor = Gajipokok + round(tunjanganIS) + round(tunjanganA)
    Gajibersih = Gajikotor - round(BesarPotongan)
    
elif(golongan == 'D'):
    Gajipokok = 5000000
    Potongan = 1.0
    BesarPotongan = Gajipokok * (Potongan / 100)
    tunjanganIS = 10 / 100 * Gajipokok
    tunjanganA = 5 /100 * Gajipokok * jumlahanak
    Gajikotor = Gajipokok + round(tunjanganIS) + round(tunjanganA)
    Gajibersih = Gajikotor - round(BesarPotongan)

    
    
print('Gaji Pokok                : Rp ' + str(Gajipokok))
print('Tunjangan Istri/Suami     : Rp ' + str(tunjanganIS))
print('Tunjangan Anak            : Rp ' + str(tunjanganA))
print('------------------------------------- +')
print('Gaji Kotor                : Rp ' + str(Gajikotor))
print('Potongan' + '(' + str(Potongan)  + '%)' + '            : Rp ' +  str(BesarPotongan))
print('------------------------------------- -')
print('Gaji Bersih               : Rp ' + str(Gajibersih))
