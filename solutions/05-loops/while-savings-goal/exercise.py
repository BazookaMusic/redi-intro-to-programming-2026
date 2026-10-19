# Savings goal
# Save 15 euros a week until you have at least 100 euros.

savings = 0
weeks = 0
while savings < 100:
    savings = savings + 15
    weeks = weeks + 1
    print(f"Week {weeks}: {savings} euros")
print(f"Goal reached in {weeks} weeks!")
