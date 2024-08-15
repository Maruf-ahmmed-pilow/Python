phone_number = "123456789-10"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(0,31):
    if i ==13:
        pass
    else:
        print(i)