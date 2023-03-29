while True:
    n = int(input())
    if n == 0:
        break

    output = ""
    for i in range(1,n+1):
        output+= str(i) + " "
    print(output[:-1])