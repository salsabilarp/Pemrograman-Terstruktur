#5 a
from operation import *

a = kali(4, 6)
b = jumlah(2, -4)
print('Hasil dari : 2 + 4*6 - 4 = ' + str(jumlah(a, b)))

#5 b
from operation import *

a = jumlah(4, 7)
b = kurang(6, 9)
print('Hasil dari : (4 + 7)*(6 - 9) = ' + str(kali(a, b)))

#5 c
from operation import *

a = bagi(jumlah(10, 2), jumlah(7, 5))
b = kurang(12, 34)
print('Hasil dari : (10 + 2)/(7 + 5)/(12 - 34) = ' + str(bagi(a, b)))
