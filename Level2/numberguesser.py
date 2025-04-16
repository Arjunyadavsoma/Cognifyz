import random

def number_guesser():
    print("Welcome to the Number Guessing Game!")
    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))
    
    if start_range >= end_range:
        print("Invalid range. Start should be less than end.")
        return
    
    random_number = random.randint(start_range, end_range)
    guess_number = None
    attempts = 0

    while guess_number != random_number:
        try:
            guess_number = int(input(f"Guess a number between {start_range} and {end_range}: "))
            attempts += 1
            if guess_number > random_number:
                print("Too high! Try again.")
            elif guess_number < random_number:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

number_guesser()
