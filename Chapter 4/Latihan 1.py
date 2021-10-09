#input data
tarifawalSewa = int(input('tarif sewa untuk 12 jam pertama Rp'))
tarifsewaBerikutnya = int(input('tarif sewa untuk per jam berikutnya Rp'))
print('MulaiSewa')
jamMulai = int(input('jam ='))
menitMulai = int(input('menit ='))
print('Mobil disewa pada pukul 06:00')
print('SelesaiSewa')
jamSelesai = int(input('jam ='))
menitSelesai = int(input('menit ='))
print('Mobil dikembalikan pada pukul 23:50')

#perhitungan lama peminjaman
lamaJamsewa = jamSelesai - jamMulai
lamaMenitsewa = menitSelesai - menitMulai

#garistambahan
print('--------------------------------------------')

#tampilkan hasil lama peminjaman
print('Total Lama Peminjaman =',lamaJamsewa,'jam',lamaMenitsewa,'menit')

#perhitungan tarif setelah 12 jam
print('Sisa waktu setelah 12 jam = 5 jam 50 menit')

#garistambahan
print('--------------------------------------------')

Totalbiayapeminjaman = 200000 + 10000*(5 + 50/60)
print('Jadi, total tarif yang harus dibayarkan kepada rental mobil sebesar Rp', Totalbiayapeminjaman)

      

