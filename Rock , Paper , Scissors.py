import random

options = ["Rock" , "Paper" , "Scissors"]

user_choice = input("Choose Rock , Paper , or Scissors : ")

computer_choice = random.choice(options)

print("You choice : " , user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
     print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
     print("Rock smashes scissors! You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
     print("paper covers rock! You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
     print("Scissors cuts paper! You win!")
else:
     print("You lose!.")
