#python problem 3 fizz buzz challenege 
#Write a program that prints the numbers from 1 to 100, except for the following conditions. 
#For multiples of three print "Fizz" instead of the number, 
#For the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".


for i in range(1,101):
	if i % 15 == 0 :
		print("FizzBuzz") 
	elif i % 3 == 0 :
		print("Fizz") 
	elif i % 5 == 0 :
		print("Buzz") 
	else:
		print(i)
            