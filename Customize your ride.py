print("Select your ride: ") 
print("1. Bike") 
print("2. Car") 

# Take input of number 1 or 2 
choice = int(input("Enter your choice: ")) 

# User choosing Bike
if choice == 1:
    print("What type of bike?") 
    print("1. Scooty") 
    print("2. Scooter") 
    choice2 = int(input("Enter your choice: ")) 

    if choice2 == 1:
        bike_type = "Scooty"
    elif choice2 == 2:
        bike_type = "Scooter"
    

    print("Where do you want to ride?")
    print("1. Inside city")
    print("2. Outside city")
    location = int(input("Enter your choice: "))
    
    if location == 1:
        print(f"You have selected {bike_type} for inside city.")
    elif location == 2:
        print(f"You have selected {bike_type} for outside city.")
    else:
        print("Invalid location choice!")

# User choosing Car
elif choice == 2:
    print("What type of car?") 
    print("1. Sedan") 
    print("2. SUV") 
    choice3 = int(input("Enter your choice: ")) 

    if choice3 == 1:
        car_type = "Sedan"
    elif choice3 == 2:
        car_type = "SUV"
    

    print("Where do you want to ride?")
    print("1. Inside city")
    print("2. Outside city")
    location = int(input("Enter your choice: "))
    
    if location == 1:
        print(f"You have selected {car_type} for inside city.")
    elif location == 2:
        print(f"You have selected {car_type} for outside city.")
    else:
        print("Invalid location choice!")

else:
    print("Wrong choice!")
