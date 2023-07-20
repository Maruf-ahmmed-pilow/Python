while True:
    a=0
    sum=0
    x= int(input())
    if x==0:
        break
    if x%2!=0:
        x+=1
    for i in range(5):
        sum+=x
        x+=2
    print(sum)
        
        
