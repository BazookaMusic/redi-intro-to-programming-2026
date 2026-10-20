# Exercise 3 (advanced): Daily weather report
# A storm skips all other advice. Clothes, rain gear, and icy roads are
# separate checks, so several lines can print.

weather = input("Weather: ").strip().lower()
temperature = int(input("Temperature: "))
wind = int(input("Wind (km/h): "))

print(f"{weather.capitalize()}, {temperature}°C, wind {wind} km/h")
if wind >= 75:
    print("Storm warning! Stay inside.")
else:
    windy = wind >= 30
    wet = weather == "rain" or weather == "snow"
    feels = temperature - 5 if windy else temperature
    if windy:
        print(f"Feels like {feels}°C")
    if feels >= 20:
        print("Wear a T-shirt.")
    elif feels >= 10:
        print("Wear a jacket.")
    else:
        print("Wear a warm coat.")
    if wet and windy:
        print("Wear a raincoat.")
    elif wet:
        print("Take an umbrella.")
    if wet and temperature < 0:
        print("Icy roads!")
