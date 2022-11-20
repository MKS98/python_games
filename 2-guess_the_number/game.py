import random

def guess(x):
    random_number = int(random.randint(1, x))
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, too high. Try again")
        elif guess < random_number:
            print("Sorry, too low. Try again")
    print(f"Excellent! {random_number} is indeed the right guess")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(H) or too low (L) or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Excellent! the computer guessed your number, {guess} ,correctly")


x = int(input("please enter the guessing range: "))
guess(x)