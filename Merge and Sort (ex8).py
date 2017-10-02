#Merge and Sort (ex8)
list1 = ['10', '30', '20', '90', '11', '5', '6']
list2 = ['1', '9', '2', '7', '3', '8', '4']

listmerger = list1 + list2

listmerger.sort(key=min)
print (listmerger)