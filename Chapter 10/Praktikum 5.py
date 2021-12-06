# file data angka
data = open('d:\listangka.txt', 'r')
read = data.readlines()

hasil = []

for mydata in read:
    split = mydata.split('|')
    bil1  = split[0]
    bil2  = split[1]

    myhasil = int(bil1) + int(bil2)
    hasil.append(myhasil)
    

data.close()

# file hasil penjumlahan dari data angka
output = open('d:\hasiljumlah.txt', 'w')

for jawab in range(len(hasil)):
    output.write(str(hasil[jawab]))
    output.write('\n')

output.close()

buka  = open('d:\hasiljumlah.txt', 'r')
print('Hasil penjumlahan bilangan pada file listangka :' + '\n' + buka.read())
