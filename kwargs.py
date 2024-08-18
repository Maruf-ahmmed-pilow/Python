from django.template.defaultfilters import first


def hello(**kwargs):
    #print("hellow " + kwargs['first'] + " " + kwargs['last'])
    print("hello",  end = " ")
    for key, value in kwargs.items():
        print(value)  


hello(first="pilot", middle = "Maruf", last='ahmed',)