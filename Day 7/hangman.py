word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

guess = input("Guess a letter: \n").lower()

for letter in chosen_word:


