#Latihan 3 Praktikum 1
BhsIndo = int(input('Nilai Bhs Indo = '))
if(BhsIndo >= 0 and BhsIndo <= 100):
    
    Mat = int(input('Nilai Mat = '))
if(Mat >= 0 and Mat <= 100):

    Ipa = int(input('Nilai Ipa = '))
if(Ipa >= 0 and Ipa <= 100):
    
    print('----------------------------------')
    
if(BhsIndo >= 60 and Mat >= 70 and Ipa >= 60):
    print('LULUS')
if(BhsIndo < 60 or Mat < 70 or Ipa < 60):
    print('TIDAK LULUS')
if(BhsIndo < 60 or Mat < 70 or Ipa < 60):
    print('Sebab :')
if(BhsIndo < 60):
    print('- Nilai Bahasa Indonesia kurang dari 60')
if(Ipa < 60):
    print('- Nilai IPA kurang dari 60')
if(Mat < 70 ):
    print('- Nilai Matematika kurang dari 70')
