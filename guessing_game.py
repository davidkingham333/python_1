import sys
import random

def valid_integer_between_1_and_100(x):
    try:
        return 1 <= int(x) <=100
    except ValueError:
        if x.lower()=="q":
            return True
        return False

def get_valid_input(prompt,error_msg,validator_function):
    while True:
        result=input(prompt)
        try:
            if validator_function(result):
                return result
        except ValueError:
            pass
        print(error_msg)

def play_guessing_game(target_value):
    my_number=target_value
    while True:
        guess = get_valid_input("enter an integer between 1 and 100(or q to exit):","that is not an integer",valid_integer_between_1_and_100)
        if (guess.lower()=="q"):
            print("goodbye")
            sys.exit()
        guess=int(guess)
        if guess < my_number:
            print("enter a higher value")
        if guess > my_number:
            print("enter a lower value")
        elif guess==my_number:
            print("you won!")


play_guessing_game(random.randint(1,100))
