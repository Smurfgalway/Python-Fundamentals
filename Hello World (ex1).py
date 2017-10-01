#helloworld exercise 1
#simple user input prints string to tell the user what value to input
user = input("Press 1 to say Hello to the World!!! ")
#if statement that will print hello world when user presses correct button. 
if int(user) == 1:
    print ("Hello World!")
    print ("Exercise 1 complete!!")
else:
    print ("Incorrect number pressed run program again")