# 1. Take a number from the user and create lists of even and odd numbers
number = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, number+1) if i % 2 != 0]
even_numbers = [i for i in range(1, number+1) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# 2. Create a list of fruits and capitalize the first letter
fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruits list:", updated_fruits)
