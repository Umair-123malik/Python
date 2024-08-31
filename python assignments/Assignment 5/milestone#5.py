import random

# Number of rounds to play
NUM_ROUNDS = 5

def high_low_game():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Initialize the user's score
    score = 0

    # Play the game for the specified number of rounds
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_number}")

        # Generate random numbers for the player and the computer
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        # Print the user's number
        print(f"Your number is {user_number}")

        # Prompt the user for their guess with input validation
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").lower()

        # Check the user's guess and update the score
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Print the current score
        print(f"Your score is now {score}")

    # Conditional ending messages based on the player's performance
    print("\nThanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    high_low_game()
