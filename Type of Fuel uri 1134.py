Alcohol = 0
Gasoline = 0
Disel = 0

while True:
    i =int(input())
    if i==1:
        Alcohol +=1
    if i == 2:
        Gasoline +=1
    if i == 3:
        Disel += 1
    if i == 4:
        break
print('MUITO OBRIGADO')
print(f'Alcool: {Alcohol}')
print(f'Gasolina: {Gasoline}')
print(f'Diesel: {Disel}')