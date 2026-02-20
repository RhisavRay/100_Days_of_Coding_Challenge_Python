import random, game_data, art


def get_article(description):
    return "an" if description[0].lower() in "aeiou" else "a"

print(art.logo)

choice1 = random.choice(game_data.data)
choice2 = random.choice(game_data.data)
while choice1 == choice2:
    choice2 = random.choice(game_data.data)

print(f"A. {choice1["name"]}, {get_article(choice1["description"])} {choice1["description"]} from {choice1["country"]}")
print(art.vs)
print(f"B. {choice2["name"]}, {get_article(choice2["description"])} {choice2["description"]} from {choice2["country"]}")

score = 0
flag = True

while flag:
    answer = "h" if choice2["follower_count"] > choice1["follower_count"] else "l"

    user_input = input("Do you think option B has more ot less followers? Type 'h' for higher or 'l' for lower: ").lower()

    if user_input != answer:
        print(f"You lose. Your score is {score}.")
        flag = False
    else:
        score += 1
        print(f"Correct answer. Your score is {score}.")
        choice1 = choice2
        choice2 = random.choice(game_data.data)
        while choice1 == choice2:
            choice2 = random.choice(game_data.data)
        print(f"A. {choice1["name"]}, {get_article(choice1["description"])} {choice1["description"]} from {choice1["country"]}")
        print(art.vs)
        print(f"B. {choice2["name"]}, {get_article(choice2["description"])} {choice2["description"]} from {choice2["country"]}")