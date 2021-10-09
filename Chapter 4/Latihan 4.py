#input data
waktuBerangkat = 06.00
print('Pak Amir berangkat dari kota A pukul 06.00')
print('Kota A ke Kota B')
jarak_AkeB = int(input('jarak dari A ke B (km) ='))
kecepatan_AkeB = int(input('kecepatan dari A ke B (km/jam) ='))
print('Kota B ke Kota C')
jarak_BkeC = int(input('jarak B ke C (km) ='))
kecepatan_BkeC = int(input('kecepatan B ke C (km/jam) =')) 
istirahat = 45
print('Istirahat di Kota B 45 menit') 

#perhitungan
waktu_AkeB = round((jarak_AkeB / kecepatan_AkeB)*60)
waktu_BkeC = round((jarak_BkeC / kecepatan_BkeC)*60)
Totalwaktu = waktu_AkeB + istirahat + waktu_BkeC
UbahkeJam = round((Totalwaktu)/60)
Sisamenit = Totalwaktu-(UbahkeJam*60)

#Waktu Tiba di Kota C
Jam = round(waktuBerangkat + UbahkeJam)
Menit = Sisamenit

#garis tambahan
print('---------------------------------------------')

print('Waktu yang diperlukan oleh pak Amir sampai ke kota C = ' + str(UbahkeJam) + 'jam' + str(Sisamenit) + 'menit')
print('Jadi, pak Amir sampai di kota C pada pukul ' + str(Jam) + ':' + str(Menit))


