import random 
import sys

print("Welcome to my Number Guessing Game!")
print("I'm going to think of a number between 1 and 100")
print("You have a different amount of chances depending of the difficulty you choose!")

number = random.randint(1, 100)

print("Please select your difficulty level: ")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

try: 
    difficulty = int(input("Enter your choice: "))
except ValueError:
    print("Please enter a number between 1-3!")
    sys.exit()

def game(tries):
    number = random.randint(1, 100)
    counter = 0
    print("The game is starting")
    for attempt in range(tries):
        counter += 1 
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("=======================================================================")
            print(f"Congratulations! You guessed the correct number in {counter} attempts")
            print("=======================================================================")
            return
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}")
        elif guess > number:
            print(f"Incorrect! The number is less than {guess}")

if difficulty == 1:
    tries = 10
    print("You have selected the Easy difficulty level.")
    game(tries)
elif difficulty == 2:
    tries = 5
    print("You have selected the Medium difficulty level.")
    game(tries)
elif difficulty == 3:
    tries = 3
    print("You have selected the Hard difficulty level.")
    game(tries)
