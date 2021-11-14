hasil = []
bilangan = []

def kuadrat():
     while True:
          try:
               bil = int(input('Masukkan data bilangan : '))
               bilangan.append(bil)
               hasil.append(bil ** 2)
          except ValueError:
               print('Harap masukkan angka')
               continue
          
          while True:
               tambah = str(input('lagi (y/n)? : '))
               if(tambah == 'y'):
                    bil = int(input('Masukkan data bilangan : '))
                    bilangan.append(bil)
                    hasil.append(bil ** 2)
               elif(tambah == 'n'):
                    bilangan.sort()
                    hasil.sort()
                    break
               else:
                    print('Input tidak valid')
                    continue
               
          
          print('List data bilangan : ', bilangan)
          print('Hasil kuadrat bilangan : ', hasil)
          break

    
kuadrat()
