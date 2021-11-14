data = []
try:
    input1 = int(input('Masukkan banyak nama mahasiswa yang kamu inginkan : '))
except ValueError:
    print('Input tidak valid')

try:
    i = 0
    while(i < (input1)):
        input2 = str(input('Masukkan nama mahasiwa : '))
        data.append(input2)
        i += 1
        continue
except ValueError:
    print('Input tidak valid')
except NameError:
    print('Data tidak ditemukan')

print('=' * 50)
data.sort()
for list in range(len(data)):
    print(data[list], '(', len(data[list]), 'karakter )')
