# Closing exercise (advanced): A fairer quiz
# Clean each text answer and use in, so close answers still count.

score = 0

freeze = int(input("At what °C does water freeze? "))
if freeze == 0:
    score = score + 1

flakes = input("What falls from clouds as frozen flakes? ").strip().lower()
if "snow" in flakes:
    score = score + 1

colours = input("What appears when the sun shines during rain? ").strip().lower()
if "rainbow" in colours:
    score = score + 1

boil = int(input("At what °C does water boil? "))
if boil == 100:
    score = score + 1

print(f"You scored {score} out of 4.")
if score == 4:
    print("Perfect forecast! ☀️")
elif score == 3:
    print("Mostly sunny! 🌤️")
else:
    print("Cloudy with a chance of revision. 🌧️")
