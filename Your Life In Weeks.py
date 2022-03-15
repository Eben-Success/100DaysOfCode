# The program requests for user's current age and
# calculates the number of x days, y weeks, and z months left.

# 365 days in a year
# 52 weeks in a year
# 12 months in a year

# This program assumes user dies at the age of 90 years

const_age = 90

current_age = input("What is your current age in years?\n")

remaining_years = const_age - int(current_age)

remaining_years = remaining_years * 365

print(f"You have {remaining_years}")
