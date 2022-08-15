# Blackjack Captone Project
import random
import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(deal_card())
    
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
