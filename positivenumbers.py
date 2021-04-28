#positive numbers
list1=[12,-7,5,64,-14]
print('List1: ',list1)
print("Positive numbers in list1:")
for i in list1:
    if i>=0:
        print(i, end=", ")
print('\n')

list2=[12,14,-95,3]
print('List2: ',list2)
print("Positive numbers in list2:")
for j in list2:
    if j<=0:
        list2.remove(j)
print(list2)

        
        

