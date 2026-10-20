# Homework 1: Five-question weather quiz
# Ask five questions, count the correct answers, and print the score.

score = 0

freeze = int(input("At what °C does water freeze? "))
if freeze == 0:
    score = score + 1

flakes = input("What falls from clouds as frozen flakes? ")
if flakes == "snow":
    score = score + 1

colours = input("What appears when the sun shines during rain? ")
if colours == "rainbow":
    score = score + 1

boil = int(input("At what °C does water boil? "))
if boil == 100:
    score = score + 1

air = input("What do you call air that moves outside? ")
if air == "wind":
    score = score + 1

print(f"You scored {score} out of 5.")
