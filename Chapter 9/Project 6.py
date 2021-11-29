nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print(('=' * 73),
      '\nNIM',
      'NAMA'.rjust(12),
      'N.MID'.rjust(12),
      'N.UAS'.rjust(12),
      'N.AKHIR'.rjust(12),
      'STATUS'.rjust(12))

print('-' * 73)

for listdata in nilai :
    
# menghitung nilai akhir
    mid = listdata.get('mid')
    uas = listdata.get('uas')
    NA = round((mid + 2 * uas) / 3)
    if NA >= 60 :
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
        
# membuat tabel data
    print(listdata['nim'].ljust(11),
          listdata['nama'].ljust(11),
          str(listdata['mid']).rjust(5),
          str(listdata['uas']).rjust(12),
          str(NA).rjust(12),
          status.rjust(12))
    
    
print('-' * 73)                          
                            
