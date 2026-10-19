# Lap counter (advanced)
# Print one line per lap, mark the last lap, then print "Race finished!".

laps = 5
for i in range(laps):
    if i + 1 == laps:
        print(f"Lap {i + 1} done - last lap!")
    else:
        print(f"Lap {i + 1} done")
print("Race finished!")
