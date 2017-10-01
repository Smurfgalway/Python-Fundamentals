# Fizz buzz Exercise 3
#number intilised as zer0
number =0;
#for that runs within a range of 100
for number in range (1, 101):
    word =""
    #if the number is a multiple of 3 it prints fizz
    if number % 3 == 0:
        word += "fizz"
    # if the number is a multiple of 5 it prints buzz
    if number % 5 == 0:
        word += "buzz"
    #if the number is not a mulitple of either it prints neither
    if word == "":
         word = number;
    #if it is a multiple of both it prints fizzbuzz
    print (word)