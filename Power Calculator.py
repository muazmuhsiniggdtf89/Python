# Power Calculator using Loops

# Input from user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Initialize result
result = 1

# Loop to calculate power
for i in range(exponent):
    result = result * base

# Output the result
print("The result is:", result)
