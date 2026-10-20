# Homework 2: Weather game show
# Two tries per question: 2 points for the first try, 1 for the second.

score = 0

freeze = int(input("At what °C does water freeze? "))
if freeze == 0:
    print("+2 points")
    score = score + 2
else:
    print("Hint: it's between -1 and 1.")
    freeze = int(input("Try again: "))
    if freeze == 0:
        print("+1 point")
        score = score + 1
    else:
        print("No points. The answer was 0.")

flakes = input("What falls from clouds as frozen flakes? ").strip().lower()
if flakes == "snow":
    print("+2 points")
    score = score + 2
else:
    print("Hint: it's white and cold.")
    flakes = input("Try again: ").strip().lower()
    if flakes == "snow":
        print("+1 point")
        score = score + 1
    else:
        print("No points. The answer was snow.")

colours = input("What appears when the sun shines during rain? ").strip().lower()
if colours == "rainbow":
    print("+2 points")
    score = score + 2
else:
    print("Hint: it has seven colours.")
    colours = input("Try again: ").strip().lower()
    if colours == "rainbow":
        print("+1 point")
        score = score + 1
    else:
        print("No points. The answer was rainbow.")

print(f"You scored {score} out of 6.")

if score == 6:
    print("Bonus question unlocked!")
    bonus = int(input("How many colours does a rainbow have? "))
    if bonus == 7:
        print("Bonus point! Final score: 7")
    else:
        print("No bonus this time.")
