# Take input from the user 
num = int(input("Enter a number: "))

power = int(input("Enter the power of the number"))
# Initialize sum 
sum = 0

# Find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

# Display the result 
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
