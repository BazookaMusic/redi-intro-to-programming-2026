# Wrong phone number
# Find the first phone number that doesn't have exactly 11 digits.

phones = ["01761234567", "01523456789",
          "01709876543", "0162345678",
          "01601234567", "015712345678"]

wrong = ""
for phone in phones:
    if len(phone) != 11:
        wrong = phone
        break

print(f"First wrong number: {wrong}")
