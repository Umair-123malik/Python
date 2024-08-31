import random

def high_low_game():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Generate random numbers between 1 and 100 for both the player and the computer
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    # Print the generated numbers for testing purposes
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

if __name__ == "__main__":
    high_low_game()
