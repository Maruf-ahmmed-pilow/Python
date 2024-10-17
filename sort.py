my_str = 'This is pilow A new atitude boy'

# for i in my_str.split():
#     w = i.sort()
#     print(w)

w = my_str.split()
for i in range(len(w)):
    w[i] = w[i].lower()

w.sort()
for i in w:
    print(i)

    
    