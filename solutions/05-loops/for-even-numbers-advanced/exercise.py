# Leap years (advanced)
# Print every leap year from 2000 to 2040, then the next one.

for year in range(2000, 2041, 4):
    print(f"{year} is a leap year")
print(f"Next leap year: {year + 4}")
