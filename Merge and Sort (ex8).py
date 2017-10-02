#Merge and Sort (ex8)
import time
list1 = ['3', '2', '4', '9']
list2 = ['5', '8', '1', '0']

list1.sort(key=max, reverse=True)
list2.sort(key=min)
listmerger = list1 + list2

listmerger.sort(key=min)
print ("list 1 as follows:",  list1, "\nlist 2 as follows:", list2)
time.sleep(1.0)
print("Merged list is as follows:", listmerger)