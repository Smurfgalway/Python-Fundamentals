# List largest and smallest (exercise 6)
basicList = ['Name', 'Age', 'Height', 'Weight', 'Nationality']

basicList.sort(key=len, reverse=True)

print("Items", basicList)