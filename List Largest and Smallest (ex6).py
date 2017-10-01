# List largest and smallest (exercise 6)
#a basic list containing strings of vareying length
basicList = ['Name', 'Age', 'Height', 'Weight', 'Nationality']

#sorts the list by character length sorted largest string first
basicList.sort(key=len, reverse=True)

#print statement that prints the list
print("Items largest to smallest in decesnding order: ", basicList)