secret_number = 7
guess = 0

while guess != secret_number:
    choose = int(input("Guess a number between 1 and 10: "))
    guess = choose

print(f"You guessed it! The secret number was {guess}")