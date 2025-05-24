actual_cost = float(input("Please Enter the Actual Product Price: "))

sale_amount = float(input("Please Enter the Sales Amount: "))

if(sale_amount > actual_cost): 
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
if(sale_amount < actual_cost): 
    amount = sale_amount - actual_cost
    print("Total Loss = {0}".format(amount))

if(sale_amount == actual_cost):
       print("No Profit and No Loss.")

    
