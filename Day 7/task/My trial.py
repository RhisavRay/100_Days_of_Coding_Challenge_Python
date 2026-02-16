import random, hangman_art, hangman_words

target_word = random.choice(hangman_words.word_list)

current_word = ""
for letter in target_word:
    current_word += "_"

# print(target_word)
# print(current_word)

lives_left = 6

print(hangman_art.logo)

while lives_left > 0:
    print(F"Word to guess: {current_word}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter")
        continue

    if guess not in target_word:
        print(f"You guessed {guess}. That's not in the word. Try again.")
        lives_left -= 1
    else:
        current_word = ""
        for letter in target_word:
            if letter == guess:
                current_word += guess
            else:
                current_word += "_"
    print(hangman_art.stages[lives_left])
    print(f"****************************** {lives_left}/6 lives left ******************************")
    if "_" in current_word:
        continue
    else:
        print("Congratulations! You win!")
        break

if lives_left == 0:
    print("Sorry, you lose")