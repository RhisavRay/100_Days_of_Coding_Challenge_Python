import random, art


cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
decision = "y"

print(art.logo)

while decision == "y":
    victory = False
    my_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards)]
    # print(my_cards)

    my_score = 0
    comp_score = 0

    for card in my_cards:
        if card == "A":
            my_score += 11
        elif card == "J" or card == "Q" or card == "K":
            my_score += 10
        else:
            my_score += int(card)

    if my_score == 22:
        my_score = 12

    for card in comp_cards:
        if card == "A":
            comp_score += 11
        elif card == "J" or card == "Q" or card == "K":
            comp_score += 10
        else:
            comp_score += int(card)

    print(f"Your cards: [{", ".join(my_cards)}]\tYour score: {my_score}")
    print(f"Dealer's card: [{", ".join(comp_cards)}]\tDealer's score: {comp_score}")

    hit = False

    if my_score < 21:
        hit = True if input("Hit/stand?: ").lower() == "hit" else False
    elif my_score == 21:
        victory = True

    while hit:
        hit = False
        new_card = random.choice(cards)
        my_cards.append(new_card)
        if new_card == "A":
            if my_score < 10:
                my_score += 11
            else:
                my_score += 1
        elif new_card == "J" or new_card == "Q" or new_card == "K":
            my_score += 10
        else:
            my_score += int(new_card)

        print(f"Your cards: [{", ".join(my_cards)}]\tYour score: {my_score}")
        print(f"Dealer's card: [{", ".join(comp_cards)}]\tDealer's score: {comp_score}")

        if my_score < 21:
            hit = True if input("Hit/stand?: ").lower() == "hit" else False
            victory = False
        elif my_score > 21:
            victory = False
        elif my_score == 21:
            victory = True

    if not victory and my_score < 21:
        while comp_score < 17:
            new_card = random.choice(cards)
            comp_cards.append(new_card)

            if new_card == "A":
                if comp_score < 10:
                    comp_score += 11
                else:
                    comp_score += 1
            elif new_card == "J" or new_card == "Q" or new_card == "K":
                comp_score += 10
            else:
                comp_score += int(new_card)

    if victory or (my_score < 21 and my_score > comp_score):
        print(victory)
        print(f"Your cards: [{", ".join(my_cards)}]\tYour score: {my_score}")
        print(f"Dealer's card: [{", ".join(comp_cards)}]\tDealer's score: {comp_score}")
        print("Congratulations! You win!")
    elif comp_score == my_score:
        print(f"Your cards: [{", ".join(my_cards)}]\tYour score: {my_score}")
        print(f"Dealer's card: [{", ".join(comp_cards)}]\tDealer's score: {comp_score}")
        print("Draw!!")
    elif not victory:
        print(f"Your cards: [{", ".join(my_cards)}]\tYour score: {my_score}")
        print(f"Dealer's card: [{", ".join(comp_cards)}]\tDealer's score: {comp_score}")
        print("Sorry, you lose!")

    decision = input("Do you want to play again? (y/n): ").lower()