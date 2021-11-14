def NAtinggi(nilaiMhs):
    nilai = 0
    for hasil in nilaiMhs:
        mid = hasil.get('mid')
        uas = hasil.get('uas')
        NA = (mid + 2 * uas) / 3
        if(NA > nilai):
            nilai = NA
            data = {}
            data['nim'] = hasil.get('nim')
            data['nama'] = hasil.get('nama')
    return data

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilaitertinggi = NAtinggi(nilaiMhs)
print('Mahasiswa yang mendapat nilai akhir tertinggi,'
      'yaitu {0} dengan NIM {1}'.format(nilaitertinggi['nama'], nilaitertinggi['nim']))
