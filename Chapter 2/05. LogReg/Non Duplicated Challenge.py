def function_whatever(list, n):
 
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and list[i] == list[j]):
                break
            j += 1
        if (j == n):
            return list[i]
     
    return -1

list = [1, 1, 2, 2, 3, 5, 5, 6, 6]
n = len(list)
print(function_whatever(list, n))

list = [1, 2, 2, 3, 3]
n = len(list)
print(function_whatever(list, n))