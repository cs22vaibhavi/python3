import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")

# Generate random number
number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break# python3