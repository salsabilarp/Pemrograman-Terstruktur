#Latihan 1 Praktikum 1
BhsIndo = int(input('Nilai Bhs Indo = '))
if(BhsIndo >= 0 and BhsIndo <= 100):
    
    Mat = int(input('Nilai Mat = '))
if(Mat >= 0 and Mat <= 100):

    Ipa = int(input('Nilai Ipa = '))
if(Ipa >= 0 and Ipa <= 100):

    print('-----------------------------------------')

if(BhsIndo >= 60 and Mat >= 70 and Ipa >= 60):
    print('LULUS')
else:
    print('TIDAK LULUS')
