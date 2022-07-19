word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

for chosen_word in word_list:
    print(chosen_word)

guess = input("Guess a letter: \n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

