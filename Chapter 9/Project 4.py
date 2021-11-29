import random

def shuffleString(kata, banyak):
    data = list(kata)
    datalist = []
    i = 0
    while i < banyak :
        acak = ''.join(random.sample(kata, len(kata)))
        if acak not in datalist:
            datalist.append(acak)
            i += 1
    print(datalist)
    

kata = str(input('Harap masukkan kata : '))
banyak = int(input('Banyaknya kata yang hurufnya diacak : '))
shuffleString(kata, banyak)
        
