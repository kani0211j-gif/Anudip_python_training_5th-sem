# Secret number selected by the game
secret_number = 7

# Repeat until correct guess is entered
while True:

    # Take guess from user
    guess = int(input("Guess the Number: "))

    # Check whether guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    # Execute when guess is wrong
    else:
        print("Wrong Guess. Try Again.")

