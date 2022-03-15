# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# If your weight falls below 18.5, you're underweight
# If it falls between 18.5 and 24.9, you're Normal or Healthy
# If it falls above 25.0, you're overweight.

weight = int(input("Enter your weight in Kilograms (Kg): \n"))

height = float(input("Enter your height in meters(m): \n"))

result = (weight/(float(height)*+2))
print(result)

print(type(height))

if result <= 18.6:
    print("You are underweight.")

elif result <= 24.9:
    print("You are normal or a healthy person")

else:
    print("You are overweight.")
