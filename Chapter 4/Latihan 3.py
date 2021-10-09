import math

#diketahui
Totalbensin = 66.25
print('Total bensin yang diperlukan pak Budi (dalam liter) =', Totalbensin)

Kapasitastangki = 50
print('Kapasitas tangki mobil pak Budi (dalam liter) =', Kapasitastangki)

#garis tambahan
print('---------------------------------------------------------------------')

#perhitungan
Minimalpengisianbensin = Totalbensin / Kapasitastangki
print('Jadi, pak Budi harus mengisi bensin hingga penuh supaya bisa menyelesaikan perjalanannya minimal', math.ceil(Minimalpengisianbensin), 'kali')

