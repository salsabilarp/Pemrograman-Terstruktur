import time
#Nomor 2
i = 0
while(i < 10):
    print('Hello World')
    i += 1

print('-----------')

#Nomor 5
i = 2
while(i <= 20):
    print('Hello World')
    i += 2

print('-----------')

#Nomor 6
i = 0
while True:
    print('Hello World')
    i += 1
    if(i == 10):
        break
    
print('-----------')

#Nomor 8
# kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while(i < baris):
    j = 0
    while(j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1

print('-----------')

#Nomor 9
# kotak bintang ajaib
kolom = 0
baris = 5

i = 0
while(i <= baris):
    j = 0
    while(j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1
    kolom += 1

print('-----------')

#Nomor 11
from random import randint
while True:
    bil = randint(0,10)
    print(bil)
    if bil == 5:
        break
    
print('-----------')

#Nomor 13
from random import randint
sum = 0
while True:
    bil = randint(0,10)
    sum = sum + 1
    print(bil)
    if bil == 5:
        break
print('Jumlah perulangan : ' + str(sum))


