#using a try and except 
try:
    number = int(input("Enter a number: "))
    print ("The number entered is", number)
#using value eror
except ValueError as ex:
    print("Exception :" , ex)
