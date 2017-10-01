#Reverse a string Exercise 10 
#reversel definition with string S
def mirrored(string):   
    #reversed string intialised 
    mirrorSt = ''

    #item that takes count of the length of the string so there starting postion is zero
    pointer = len(string)
    #while the pointers position is greater than 0 the while continues
    while pointer > 0:
        mirrorSt += string[ pointer - 1 ]
        pointer = pointer - 1
    return mirrorSt
#print statement that prints the set word reversed
print(mirrored('Sham'))