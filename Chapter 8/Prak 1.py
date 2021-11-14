data = []
try:
    input1 = int(input('Masukkan banyak bilangan yang kamu inginkan : '))
except ValueError:
    print('Input tidak valid')

try:
    i = 0
    while(i < input1):
        input2 = int(input('Masukkan bilangan yang kamu pilih :'))
        data.append(input2)
        i += 1
        continue
except ValueError:
    print('Input tidak valid')

print('=' * 50)
data.sort(reverse = True)
print('Hasil list data : ', data)
