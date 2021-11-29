def bintang (n):
    for x in range (0, n):
        for y in range (0, x + 2):
            rumus = '*' * (1 + ((y-1)*2))
        print(rumus.center(20))

n = int(input('Banyak baris bintang : '))
bintang(n)
