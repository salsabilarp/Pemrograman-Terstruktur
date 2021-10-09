#diketahui
Totaljarak = int(input('Jarak kota A sampai kota C (dalam km) ='))
KonsumsiBBM = int(input('Konsumsi bbm per liter dapat menempuh jarak (dalam km) ='))

#garis tambahan
print('-----------------------------------------------------------------------')

#perhitungan
Bensinyangdiperlukan = Totaljarak / KonsumsiBBM
print('Jadi, bensin yang diperlukan pak Budi untuk perjalanan sebanyak', Bensinyangdiperlukan, 'liter')
