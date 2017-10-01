#Reverse a string Exercise 10 
def mirrored(string):
    
    mirrorSt = ''
    pointer = len(string)
    while pointer > 0:
        mirrorSt += string[ pointer - 1 ]
        pointer = pointer - 1
    return mirrorSt
print(mirrored('Sham'))