def print_pyramid(n):
    k = 2*n - 2
    for i in range(0, n):

        for j in range(0, k):
            print(end=' ')
        
        k = k - 2

        for j in range(0, i+1):

            print('#',end ='')

        print('\r')

n= 5
print_pyramid(5)