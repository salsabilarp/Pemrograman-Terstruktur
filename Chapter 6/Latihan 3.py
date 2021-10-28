#3a
def faktorial(n):
    n_faktorial = 1
    while(n > 0):
        n_faktorial = n_faktorial * n
        n -= 1
    return n_faktorial

#menghitung kombinasi
def C(n, r):
    Rumus = faktorial(n) / faktorial(r) * faktorial(n - r)
    return Rumus

n = 5
r = 3
print('Hasil dari C(' + str(n) + ', ' + str(r) + ') adalah ' +  str(C(n, r)))

#menghitung permutasi
def P(n, r):
    Rumus = faktorial(n) / faktorial(n - r)
    return Rumus

n = 10
r = 7
print('Hasil dari P(' + str(n) + ', ' + str(r) + ') adalah ' + str(P(n, r)))
 
