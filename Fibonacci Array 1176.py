T = int(input())

for i in range(T):
    N = int(input())
    
    sequence = [0, 1]
    
    for j in range(N):
        
        result = sequence[-1] + sequence[-2]
        sequence.append(result)
        
    print(f'Fib({N}) = {sequence[N]}')