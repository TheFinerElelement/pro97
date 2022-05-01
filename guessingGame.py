import random
print("number guessing game. guess a number between 1-9")
number=random.randint(1,9)
chances=0
print("Guess a number from 1-9")
while chances<5:
    guess=int(input("enter your guess: "))
    if guess==number:
        print("Congrats you won!")

    elif guess<number:
        print("your guess was too low. guess something higher than",guess)

    else:
        print("your number is too high. guess something lesser than",guess)

    chances=chances+1

if not chances<5:
    print("you lost. the number was",number)
    