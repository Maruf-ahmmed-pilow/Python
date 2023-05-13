# n=int(input())
# if 0<n<13:
#     fact = 1
#     for i in range(1, n+1):
#         fact=fact*i

# print(fact)


################


N = int(input()) 

factorial = 1 


for i in range(2, N+1):
    factorial *= i

print(factorial) 
