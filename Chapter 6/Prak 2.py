#Nomor 2
def luasSegitiga(a,t):
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(alas,tinggi))

#Nomor 4
def luasSegitiga2(a,t):
    luas = a * t / 2
    print('Luas segitiga dg alas ', a,
      ' dan tinggi ', t,
      ' adalah ', luas)

alas = 10
tinggi = 20
luasSegitiga2(alas,tinggi)

#Nomor 6
def luasSegitiga(a,t):
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
ALAS = 15
TINGGI = 45
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(alas,tinggi))
print('Luas segitiga dg alas ', ALAS,
      ' dan tinggi ', TINGGI,
      ' adalah ', luasSegitiga(ALAS,TINGGI))

#Nomor 7
def luasSegitiga2(a,t):
    luas = a * t / 2
    print('Luas segitiga dg alas ', a,
      ' dan tinggi ', t,
      ' adalah ', luas)

alas = 10
tinggi = 20
ALAS = 15
TINGGI = 45
luasSegitiga2(alas,tinggi)
luasSegitiga2(ALAS,TINGGI)

#Nomor 8
def luasSegitiga(a,t):
    luas = a * t / 2
    return luas
def jadi():
    print('Luas segitiga dg alas ', alas, ' dan tinggi ', tinggi, ' adalah ', luasSegitiga(alas, tinggi))

alas = 10
tinggi = 20
LUAS1 = luasSegitiga(alas, tinggi)
jadi()
alas = 15
tinggi = 45
LUAS2 = luasSegitiga(alas, tinggi)
jadi()
total = LUAS1 + LUAS2
print('Total luas kedua Segitiga tersebut adalah ' + str(total))

