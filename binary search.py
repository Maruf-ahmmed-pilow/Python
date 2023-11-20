a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,22,24,]

item = int (input())
left = 0
right = len(a)-1

while True:
    middle = (left+right)//2
    if  (a[middle] == item):
        print('Item found at index', middle)
        exit()
        
    elif (a[middle] < item) : 
        left = middle + 1
    else:
        right = middle - 1
print("item not found")
