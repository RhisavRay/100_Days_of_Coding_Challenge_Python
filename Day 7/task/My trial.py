import random, hangman_words, hangman_art

target_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

current_word = ""
for letter in target_word:
    current_word += "_"

lives_left = 6
given_inputs = ""

while lives_left > 0 and "_" in current_word:
    print(f"Word to guess: {current_word}")
    user_input = input("Guess a letter: ").lower()

    if len(user_input) != 1:
        print("Please enter a single letter")
        continue

    if user_input in given_inputs:
        print("You have already used this character. Try a new one")
    else:
        given_inputs += user_input
        if user_input not in target_word:
            lives_left -= 1
            print(f"You guessed {user_input}. That's not in the word. Try again.")
        else:
            new_word = ""
            for i in range(len(target_word)):
                if target_word[i] == user_input:
                    new_word += target_word[i]
                else:
                    new_word += current_word[i]
            current_word = new_word

        print(hangman_art.stages[lives_left])
        print(f"****************************** {lives_left}/6 lives left ******************************")

if lives_left == 0:
    print(f"\n\n\tSorry. You lost. The word was {target_word}")
else:
    print("\n\n\tCongratulations! You won!")