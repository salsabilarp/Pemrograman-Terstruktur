# membuka dan membaca baris pada file
file = open('d:/angka.txt', 'r')
mylist = file.readlines()

# menentukan jumlah bilangan ganjil dan genap
sum = 0
x = 0
for data in mylist:
    rumus = int(data)% 2
    if rumus == 0 :
        sum += 1
    if rumus != 0:
        x += 1

print('Banyaknya bilangan genap = ', sum)
print('Banyaknya bilangan ganjil = ', x)


