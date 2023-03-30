a = list(map(int, input().split()))


A = a[0]
N = a[-1]

total = [A]

for i in range(1, N):
    A +=1
    total.append(A)

result = sum(total)
print(result)
