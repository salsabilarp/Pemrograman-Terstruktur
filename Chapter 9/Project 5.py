nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print(('=' * 50),
      '\nNIM',
      'NAMA'.rjust(13),
      'N.MID'.rjust(13),
      'N.UAS'.rjust(13))

print('-' * 50)

for listdata in nilai :
    print(listdata['nim'].ljust(12),
          listdata['nama'].ljust(12),
          str(listdata['mid']).rjust(5),
          str(listdata['uas']).rjust(13))
    
print('-' * 50)                          
                            
