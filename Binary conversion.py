#input the decimal number from the user
num =int(input("Enter a decimal number :"))

#empty string to store the binary number
binary = ""

#if the number is 0
if num == 0:
    binary = "0"

else:
#repeat until the number becomes 0
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

#the result
print("Binary number is :" ,binary)
