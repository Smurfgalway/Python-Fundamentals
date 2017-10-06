# Squart Root (ex 9)
import math

sq = 10.0

#using the built in python maths function its returns the square root
print("Using Math Sq root function the square root returns: \n", math.sqrt(sq))

#defintion takes in set number and using newtons method returns the square root
def newtonSqrt(num):
	    root = 0.5 * num
	    z_next = 0.5 * (root + num/root )
	    while z_next != root:
	        root = z_next
	        z_next = 0.5 * (root + num/root)
	    return root	
print("Using Newtons method the square root returns: \n" , newtonSqrt(10))