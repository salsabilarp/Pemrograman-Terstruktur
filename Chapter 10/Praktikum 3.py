# membuka dan membaca file
file = open('d:/listdata.txt', 'r')
read = file.readlines()

mydict = {}
List = []
mylist = list(read)

for listdata in mylist:
    split = listdata.split('|')
    nim = split[0]
    nama = split[1]
    alamat = split[2].replace('\n', '')

    Dict = {'nim' : nim, 'nama' : nama, 'alamat' : alamat}
    List.append(Dict)

print('Data Mahasiswa : ', List)
file.close



     

