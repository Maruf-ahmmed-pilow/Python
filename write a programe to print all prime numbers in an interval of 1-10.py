lower = 1
upper = 10

print(f'prime numbers between {lower} and {upper} are:')

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

print('new line of code:')

#_____________________or________________________

for num in range(1, 11):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)