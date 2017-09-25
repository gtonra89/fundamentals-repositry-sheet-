#pythonproblem 4 
#Write a function that calculates the sum of the digits of the factorial of a number. 
#n! means n x (n − 1) ... x 3 x 2 x 1. For example, 
#10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, 
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
#Find the sum of the digits in the number 100!
import math
def FactSum(n):
    x=math.factorial(n) # gets the factorial of the number in the value of n
    print("the facrtorail of the number:" ,n,"is :",x)
    a=str(x)#converts number to string
    print("this is A:",a)
    b = [int(d) for d in str(a)] #convert back string split into a array of ints
    print("this is b :",b) 
    ##sum(b) # sum the array of ints to get your'e sum
    print("the factorial Sum is :",sum(b))

FactSum(n=10) #calling the above function
