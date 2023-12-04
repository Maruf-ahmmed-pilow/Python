#List comprehension
list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_list1 = []
for i in list1:
    new_list1.append(i+1)
print(new_list1)


#with list comprehension

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

new_list2 = [i+1 for i in list2]
print(new_list2)