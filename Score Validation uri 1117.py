a=[]
while True:
    for i in range(1):
        x = float(input())

        if 0<=x<=10:
            a.append(x)

        else:
            print('nota invalida')
    if len(a)==2:
        avg=sum(a)/2
        print(f"media ={avg:.2f}")
        break
