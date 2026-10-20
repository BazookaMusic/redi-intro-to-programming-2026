# Exercise 3: Weather advisor
# Choose clothes from the warmest down, then check for rain separately.

temperature = int(input("Temperature: "))
rain = input("Is it raining? (yes/no) ").strip().lower()

if temperature >= 20:
    print("Wear a T-shirt.")
elif temperature >= 10:
    print("Wear a jacket.")
else:
    print("Wear a warm coat.")

if rain == "yes":
    print("Take an umbrella.")
