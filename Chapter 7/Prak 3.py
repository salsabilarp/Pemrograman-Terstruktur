try:
    file = open("d:/data2.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print('Maaf ada data yang bukan bilangan sehingga tidak bisa melakukan penjumlahan')
