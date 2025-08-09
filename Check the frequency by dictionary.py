# Smaple dictionary
test_dict = {'a' : 3, 'b' : 2, 'c' : 3, 'd' : 2, 'e' : 3}

# Value whose frequency we want to check 
check_value = 3

# Count frequency
frequency = list(test_dict.values()).count(check_value)

print("The frequency of" , check_value, "is", frequency)
