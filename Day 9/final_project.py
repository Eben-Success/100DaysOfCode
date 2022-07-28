from art import logo
import os

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"Eben":456, "James":123}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            #winner =
            # TODO There is problem here I need to find the highest bid
        print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: \n")
    price = int(input("What is your price?: $ \n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        continue
