#Palindrome test (ex7)

#time import purely for aesthethic 
import time;
#User given string to be tested to see if it is a palindrome
word = input('enter word ')

#reverses the string so it can be compared 
mirrorWord = reversed(word)

#message to tell the user the test has begun
print ('..testing for palindrome..')
#short 1 second print delay for aesthethic reasons
time.sleep(1.0)

#if statement to test that when reverse the given word is still the same and infact a Palindrome
if list(word) == list(mirrorWord):
    print (word, "is a Palindrome!")
else:
    print (word, "is not Palindrome!")