a = 'pilow'
print(a[::-1])
print(a[-1])


#____________ usong function


def reverse(s):
    return s[::-1]

print(reverse('pilow'))


def reverse_string(s):
    reverse_text = " "
    for char in s:
        reverse_text = char + reverse_text
    return reverse_text

print(reverse_string('pilow'))