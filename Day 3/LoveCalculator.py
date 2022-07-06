
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
print("Total is: " + true)

l = lowwer_case_string.count("l")
o = lowwer_case_string.count("o")
v = lowwer_case_string.count("v")
e = lowwer_case_string.count("e")