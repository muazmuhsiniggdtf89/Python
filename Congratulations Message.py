name = input("Enter the name: ")
achievement = input("Enter the achievement: ")

# Prepare variations using .format()
message1 = "Congratulations {name}! You did an amazing job on your {achievement}!".format(name=name, achievement=achievement)
message2 = "Hats off to you, {name}, for achieving such a wonderful {achievement}.".format(name=name, achievement=achievement)
message3 = "{name}, success like yours deserves to be celebrated! Cheers on your {achievement}!".format(name=name, achievement=achievement)
message4 = "{} – your {} is truly inspiring. Congratulations!".format(name.upper(), achievement)

# Display all messages
print(message1)
print(message2)
print(message3)
print(message4)
