x = 0
y = 0
z = 0

while True:
    x = int(input())
    if(x >= 0):
        y += x
        z += 1
    else:
        break

print("%.2f" %(y/float(z)))