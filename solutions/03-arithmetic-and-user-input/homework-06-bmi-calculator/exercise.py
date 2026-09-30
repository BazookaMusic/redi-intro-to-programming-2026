# Homework 6: BMI calculator
# Ask for weight and height, then print BMI rounded to 1 decimal place.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = weight / height ** 2
print("BMI:", round(bmi, 1))
