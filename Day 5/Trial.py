# Create a PyPassword Generator from scratch.

import random

letters = letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome PyPassword Generator")

nr_letters = input("Enter the number of letters\n")
nr_numbers = input("Enter the number of numbers\n")
nr_symbols = input("Enter the number of symbols\n")

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

print(password_list)