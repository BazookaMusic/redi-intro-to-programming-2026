# Wrong phone number (advanced)
# Find the first phone number that doesn't have exactly 11 digits,
# and its position in the list.

phones = ["01761234567", "01523456789",
          "01709876543", "0162345678",
          "01601234567", "015712345678"]

wrong = ""
position = 0
for phone in phones:
    position = position + 1
    if len(phone) != 11:
        wrong = phone
        break

if wrong == "":
    print("All numbers look fine")
else:
    print(f"First wrong number: {wrong} (position {position})")
