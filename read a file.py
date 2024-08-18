with open("test.txt") as file:
    print(file.read())


#write a file
text = "YO\n"
with open('test.txt', 'w') as file:
    file.write(text)