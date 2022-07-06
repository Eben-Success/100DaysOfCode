height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")

