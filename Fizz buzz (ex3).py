# Fizz buzz Exercise 3

number =0;

for number in range (1, 101):
    s =""
    if number % 3 == 0:
        s += "fizz"
    if number % 5 == 0:
        s += "buzz"
    if s == "":
         s = number;
    print (s)