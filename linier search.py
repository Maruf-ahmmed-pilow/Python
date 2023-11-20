# def linear_search(L,x):
#     n = len(L)
#     i = 0
# #___using while loop____
#     while i<n:
#         if L[i] == x:
#             return i
        
#         i+=1
#     i=-1
#     return i


# #____________using for loop____________

# def linear_search(L,x):
#     n = len(L)
    
#     for i in range(n):
#         if L(i) == x:
#             return i
        
#     return -1


#______________________

def linear(arr,n,item):
    for i in range(0,n):
        if (arr[i] == item):
            return i
    return -1


# Driven / main code
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
item = int(input())

index=linear(arr,n,item)
if (index == -1):
    print("Item not found")
    
else:
    print('Item found at index', index)

 