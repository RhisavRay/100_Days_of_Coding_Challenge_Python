# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from platform import system

import art

print(art.logo)

any_other = "yes"
bids = {}

while any_other == "yes":
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")

    bids[name] = int(bid)

    any_other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 30)

winner = ""
winning_bid = 0
for name in bids:
    if bids[name] > winning_bid:
        winner = name
        winning_bid = bids[name]

print(f"The winner is {winner} with a bid of ${winning_bid}")