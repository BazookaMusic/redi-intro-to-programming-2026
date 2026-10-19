# Cubes between 10 and 500 (advanced)
# Skip cubes smaller than 10 and stop at the first cube bigger than 500.

for n in range(1, 100):
    cube = n * n * n
    if cube < 10:
        continue
    if cube > 500:
        print(f"Stopped at {n}")
        break
    print(f"{n} * {n} * {n} = {cube}")
