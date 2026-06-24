import random

secret_number = random.randint(1,10)
guesses = 0

print("Welcome to the Guess the Number Game!") 

while True:
    guess = int(input("Please guess a number between 1 and 10: "))
    guesses +=1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {guesses} guesses.")
        break


