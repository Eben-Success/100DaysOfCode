
# This program test the compatibility between two people.

print("Welcome to the Love Calculator\n")

name1 = input("What is your name?: \n")
name2 = input("What is their name?: \n")

combined_string = name1 + name2
lowwer_case_string = combined_string.lower()

t = lowwer_case_string.count("t")
r = lowwer_case_string.count("r")
u = lowwer_case_string.count("u")
e = lowwer_case_string.count("e")

true = t + r + u + e
print("Total is: " + str(true))

l = lowwer_case_string.count("l")
o = lowwer_case_string.count("o")
v = lowwer_case_string.count("v")
e = lowwer_case_string.count("e")

love = l+o+v+e
print("Total is: " + str(love))

love_score = str(true) + str(love)
print("Your score is: " + love_score)

if (love_score) < 10 or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")

else:
    print(f"Your score is {love_score}.")