import random

def rock_sizers_paper():
    choices = ["rock", "sizers", "paper"]

    while True:
        user_choice = input("Enter rock, sizers, or paper (or q to quit): ").lower()

        if user_choice == "q":
            print("Game ended.")
            break

        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            print(f"Both chose {user_choice}. It's a tie!")
        elif user_choice == "rock" and computer_choice == "sizers":
            print("Rock crushes sizers! You win!")
        elif user_choice == "sizers" and computer_choice == "paper":
            print("Sizers cut paper! You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print(f"{computer_choice} beats {user_choice}! You lose!")

rock_sizers_paper()


