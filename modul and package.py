# import datetime 
# today = datetime.datetime.today()
# print(today)


# from datetime import datetime 
# d = datetime.today()
# print(d)

# import webbrowser
# url = 'http://subeen.com'
# webbrowser.open(url)

#----------new model----------

def find_fib(n):
    if n < 2:
        return 1
    
    fib_x, fib_next = 1, 1
    
    i = 3
    while i<=n:
        i+=1
        fib_x, fib_next = fib_next,fib_x + fib_next
        return fib_x
    
    for x in range(1,11):
        print(find_fib(x))