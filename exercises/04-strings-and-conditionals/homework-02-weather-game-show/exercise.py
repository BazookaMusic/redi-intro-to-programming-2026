# Homework 2: Weather game show
# Turn the three-question weather quiz into a game show.
# Clean every text answer with .strip().lower() before you check it.
#
# For each question:
# - Correct on the first try: print "+2 points" and add 2 to score.
# - Wrong: print the hint, then ask again with input("Try again: ").
#   - Correct now: print "+1 point" and add 1 to score.
#   - Still wrong: print "No points. The answer was [answer]."
#
# Questions, answers, and hints:
# 1. At what °C does water freeze?                  -> 0
#    Hint: it's between -1 and 1.
# 2. What falls from clouds as frozen flakes?       -> snow
#    Hint: it's white and cold.
# 3. What appears when the sun shines during rain?  -> rainbow
#    Hint: it has seven colours.
#
# After the three questions, print "You scored [score] out of 6."
# If the score is 6, print "Bonus question unlocked!" and ask:
# How many colours does a rainbow have?             -> 7
# - Correct: print "Bonus point! Final score: 7"
# - Wrong: print "No bonus this time."
#
# Example input: 0, rain, snow, rainbow
# Example output:
# +2 points
# Hint: it's white and cold.
# +1 point
# +2 points
# You scored 5 out of 6.
#
# Write your solution below.
