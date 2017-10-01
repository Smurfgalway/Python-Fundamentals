#Merge and Sort (ex8)
list1 = ['b', 'd', 'a', 'c', 'x', 'z', 'y']
list2 = ['1', '9', '2', '7', '3', '8', '4']

list1.sort(key=len)
list2.sort(key=len)


listmerger = list1 + list2

print (listmerger)