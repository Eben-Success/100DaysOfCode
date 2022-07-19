import random
from logo import logo
from word_list import

word_list = ["realmadrid", "barcelona", "chelsea", "arsenal"]

chosen_word = random.choice(word_list)

# Test the code by checking the random number
print(f'\n Ops, the right word is {chosen_word} \n')

word_length = len(chosen_word)

# Display dashes equal to the random letter the user
# has to guess

display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    # Request for a letter from user
    guess = input("\nGuess a number \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
