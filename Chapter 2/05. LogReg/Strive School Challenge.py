def strive_school(a):
    for k in a:
        if  k%3==0 and  k%5==0:
            print('striveschool')
        elif  k%3==0:
            print('strive')
        elif  k%5==0:
            print('school')
        else:
            print(k)
    

a = [1,2,3,5,15]
strive_school(a)