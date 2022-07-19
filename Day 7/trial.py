import random
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