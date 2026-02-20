import random

print("Welcome to the number guesser game")

print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

number = random.randint(1,100)
guesses = 5 if difficulty == 'hard' else 10

guess = 0

while guesses != 0:
    print(f"You have {guesses} attempts left to guess the number")
    guess = int(input("Make a guess: "))
    guesses -= 1
    if guess == number:
        guesses += 1
        print(f"You guessed the number! it was {guess}")
        break
    elif guess < number:
        print(f"Your guess was too low")
    elif guess > number:
        print(f"Your guess was too high")

if guesses == 0:
    print("You lost")
else:
    print("You win")