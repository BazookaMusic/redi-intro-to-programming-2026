# Savings goal (advanced)
# Save 10 euros in week 1, then 5 more each week, until you have at least 100.

savings = 0
weeks = 0
amount = 10
while savings < 100:
    savings = savings + amount
    weeks = weeks + 1
    print(f"Week {weeks}: saved {amount}, total {savings} euros")
    amount = amount + 5
print(f"Goal reached in {weeks} weeks!")
