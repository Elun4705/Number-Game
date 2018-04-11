import random
i = random.randrange(1,100)
print("Welome to number guessing name! Guess a number between 1 and 100:")
attempts = 0
#player input
guess = input("Guess:")
while attempts <= 5:
    if int(guess) == i:
        print("Right on! Good job! You guessed correctly!")
    elif int(guess) > i:
        print("Too high! Guess again...")
        guess = input("Guess:")
    elif int(guess) < i:
        print("Too low! Guess again...")
        guess = input("Guess:")
    attempts = attempts+1
    if attempts == 5:
        print("Sorry...You are a failure at this game, here is the number " + str(i) + "... Don't come back... Just kidding! Go ahead and retry... if you dare.")
