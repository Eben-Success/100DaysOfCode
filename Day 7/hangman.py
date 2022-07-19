word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}')

display = []
for letter in chosen_word:
    display += "_"
print(display)

# Alternative approach

len_chosen_word = len(chosen_word)

for i in range(0, len_chosen_word + 1):
    print()

guess = input("Guess a letter: \n").lower()

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

