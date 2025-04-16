import random

def guess_number():
    number = random.randint(1, 100)
    attempt = 0
    guess = None

    print("Guess the number between 1 and 100!")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempt += 1

            if guess < number:
                print("Too Low.")
            elif guess > number:
                print("Too High.")
            else:
                print("Congratulations! You guessed the correct number.")
                print(f"Total attempts: {attempt}")
        except ValueError:
            print("Please enter a valid integer between 1 and 100.")

guess_number()
