# Clean shopping list (advanced)
# Skip blank items and print the others cleaned up.

items = [" milk", "", "bread ", "   ", "eggs"]

for item in items:
    clean = item.strip()
    if clean:
        print(clean.capitalize())
