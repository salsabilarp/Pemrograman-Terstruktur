from datetime import *

def diffDate(x):
    split  = x.split('-')
    tahun  = int(split[0])
    bulan  = int(split[1])
    hari   = int(split[2])
    tgl = date(tahun, bulan, hari)
    today  = datetime.date(datetime.now())
    selisih = tgl - today
    hasil = selisih.days
    print(hasil)

    return(hasil)
    
x = diffDate('2021-12-31')
