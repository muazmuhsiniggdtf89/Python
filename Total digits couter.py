# Take input from the user
number = int(input("Enter a number: "))

# Make the number positive to handle negative input
if number < 0:
    number = -number

# Initialize counter
count = 0


if number == 0:
    count = 1
else:
    # Count digits using while loop
    while number > 0:
        number = number // 10
        count += 1

# Display the result
print("Total number of digits:", count)
