mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']


print(('=' * 68),
      '\nNIM',
      'NAMA MAHASISWA'.rjust(22),
      'TGL LAHIR'.rjust(18),
      'TEMPAT LAHIR'.rjust(20))
print('-' * 68)

for listdata in mhs :
    split = listdata.split(':')
    nim = split[0]
    nama = split[1]
    tempat = split[3]
    
# mengubah urutan tanggal lahir
    tgl = split[2]
    tglnew = tgl.split('-')
    urutan =  tglnew[2] + '/' + tglnew[1] + '/' + tglnew[0]
    
    print(nim.ljust(11),
          nama.ljust(23),
          urutan.ljust(17),
          tempat.ljust(10))

print('-' * 68)
    
    
    
