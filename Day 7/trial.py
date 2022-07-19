import random
word_list = ["realmadrid", "barcelona", "chelsea", "arsenal"]

chosen_word = random.choice(word_list)

print(f'Ops, the right word is {chosen_word}')

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)