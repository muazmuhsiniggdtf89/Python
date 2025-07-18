try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    else:
        print("Valid age entered.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
