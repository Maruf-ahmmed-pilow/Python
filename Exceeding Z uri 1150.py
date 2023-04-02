X = int(input())

while True:
    Z = int(input())

    if Z > X:
        break
result = 0
count = 0

for i in range(X, Z):
  
    result +=i
    count +=1

    if result > Z:
        break

print(count)




