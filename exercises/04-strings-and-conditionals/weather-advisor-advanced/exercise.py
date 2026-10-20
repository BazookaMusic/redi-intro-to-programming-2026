# Exercise 3 (advanced): Daily weather report
# Ask for the weather (like rain, snow, or sun), the temperature,
# and the wind speed in km/h. Clean the weather with .strip().lower().
#
# First, print a summary line like: Rain, -1°C, wind 40 km/h
# Then:
# - wind 75 or more: print "Storm warning! Stay inside." and nothing else
# - wind 30 or more: it feels 5° colder. Print "Feels like [number]°C"
#   and choose clothes for that temperature
# - clothes: 20° or more -> Wear a T-shirt.
#            10° to 19°  -> Wear a jacket.
#            below 10°   -> Wear a warm coat.
# - rain or snow: print "Take an umbrella."
#   or "Wear a raincoat." instead if the wind is 30 or more
# - rain or snow below 0° (the real temperature): also print "Icy roads!"
#
# Example input: " RAIN ", -1, 40
# Example output:
# Rain, -1°C, wind 40 km/h
# Feels like -6°C
# Wear a warm coat.
# Wear a raincoat.
# Icy roads!
#
# Write your solution below.
