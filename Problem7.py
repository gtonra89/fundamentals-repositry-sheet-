# Program to check if a string is a palindrome or not

# change this value for a different output
def palTest(str):
# make it suitable for caseless comparison
    myString = str.casefold()
# reverse the string
    reverseString = reversed(myString)
# check if the string is equal to its reverse
    print("string to check :",myString)
    if list(myString) == list(reverseString):
        print("It is palindrome")
    else:
        print("It is not palindrome")

myString = 'abaBA' #declare string
palTest(myString)  #call function pass string