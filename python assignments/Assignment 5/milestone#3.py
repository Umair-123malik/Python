import random

def high_low_game():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Generate random numbers between 1 and 100 for both the player and the computer
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)

    # Print the user's number (the computer's number will remain hidden for now)
    print(f"Your number is {user_number}")

    # Prompt the user for their guess
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Check the user's guess
    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

if __name__ == "__main__":
    high_low_game()
