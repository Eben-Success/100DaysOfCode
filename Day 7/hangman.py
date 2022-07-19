word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}')

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)
guess = input("Guess a letter: \n").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)