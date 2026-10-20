# Closing exercise: Weather quiz
# Add 1 to score for each correct answer, then print the total.

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

print(f"You scored {score} out of 3.")
