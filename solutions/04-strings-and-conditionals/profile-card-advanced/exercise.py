# Exercise 1 (advanced): Full profile card
# Clean the answers, build the title, line, and username, then print the card.

first = input("First name: ").strip().capitalize()
last = input("Last name: ").strip().capitalize()
year = int(input("Birth year: "))
city = input("City: ").strip().capitalize()
hobby = input("Hobby: ").strip().capitalize()
bio = input("Short bio: ").strip()

title = f"{first} {last}"
line = "=" * len(title)
username = title.lower().replace(" ", "_")

print(f"""{title.upper()}
{line}
👤 @{username}
🎂 {2026 - year} years old
📍 {city}
❤️ {hobby}
📝 {bio}""")
