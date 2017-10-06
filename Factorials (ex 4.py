#Factorials Exercise 4
import math

factorial = math.factorial(100)
# getting the factorial of 100
print ("The factorial of 100 = \n", factorial)

#list of ints in 100
Nums = [int(x) for x in str(factorial)]

#summing all of the numbers in 100
print("The sum of all the numbers in 100 are " , sum(Nums))