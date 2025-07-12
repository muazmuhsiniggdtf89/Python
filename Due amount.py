# Take input from the user
total_bill = int(input("Enter the total bill amount: "))
amount_paid = int(input("Enter the amount paid by the customer: "))

# Calculating due amount
due_amount = total_bill - amount_paid

# Show result using normal print
if due_amount > 0:
    print("The customer still needs to pay:", due_amount, "Tk")
elif due_amount < 0:
    print("Extra paid:", -due_amount, "Tk (Give back to the customer)")
else:
    print("The bill is fully paid. No due.")
