n = int(input())


list_x = list(map(int, input().split()))

min_val = min(list_x)
print(f"Menor valor: {min_val}")

index_min_val = list_x.index(min_val)
print(f"Posicao: {index_min_val}")