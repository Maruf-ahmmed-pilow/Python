from audioop import reverse

name = "maruf ahmed pilow"
first_name = name[0:11]
last_name = name[12:17]
funky_name = name[::3]
reverse_name = name[::-1]


website1 = "http://google.com"
website2 = "http://facebook.com"

slice = slice(7,-4)

print(website2[slice])
print(website1[slice])
print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)