def bintang (n):
    for x in range (n):
        for y in range (0, x + 2):
            rumus = '*' * (1 + ((y-1)*2))
        print(rumus.center(30))

def formasi(n):
    for i in range (n):
        for j in range (0, i + 2):
            cara = '*' * (n - (2*j))
        print(cara.center(30))

def formasibintang(n):
    while True:
        if(n % 2 == 0):
            print('input tidak valid')
            n = int(input('Masukkan bilangan ganjil : '))
        else:
            bintang(n//2+1)
            formasi(n)
            break

n = int(input('Masukkan bilangan ganjil : '))

formasibintang(n)
 
