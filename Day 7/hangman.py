word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}')

guess = input("Guess a letter: \n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

