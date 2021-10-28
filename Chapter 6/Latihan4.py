#function sum
def sum(*n):
    i = 0
    for x in n:
        i = i + x
    print('Jumlah total dari data di atas adalah ' + str(i))

#function average
def average(*n):
    i = 0
    banyak = 0
    for x in n:
        banyak = banyak + 1
        i = (i + x) / banyak
    print('Hasil rata-rata dari data di atas adalah ' + str(i))

#function maks
def maks(*n):
    maks = n[0]
    for bil in n:
        if bil > maks:
            maks = bil
    print('Nilai maksimum dari data di atas adalah ' + str(maks))
    
#function min
def min(*n):
    min = n[0]
    for bil in n:
        if bil < min:
            min = bil
    print('Nilai minimum dari data di atas adalah ' + str(min))   

