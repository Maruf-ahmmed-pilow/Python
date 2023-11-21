def bubble_sort(L):
     n = len(L)
     
     for i in range(0, n):
         for j in range(0, n-i-1):
             if L[j] > L[j+1]:
                 L[j], L[j+1] = L[j+1], L[j]
                 
                 
if __name__ == '__main__':
    L=[1,2,3,34,32,11,55,66,76,22]
    print('Before sort: ', L)
    bubble_sort(L)
    print('After sort', L)
        