def starFormation1(n):
    x = 0
    i = 0
    while(i <= n):
        j = 0
        while(j < x):
            print('* ', end='')
            j += 1
        x += 1
        print('')
        i += 1
        
starFormation1(4)
print('-------------------')

def starFormation2(n):
    x = 4
    i = 0
    while(i < n):
        j = 0
        while(j < x):
            print('* ', end='')
            j += 1
        x -= 1
        print('')
        i += 1
        
starFormation2(4)
print('-------------------')

def starFormation3(n):
    starFormation1(3)
    starFormation2(4)

starFormation3(7)
