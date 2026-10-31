def slices_left(slices, eaten):
    return slices - eaten


remaining = slices_left(8, 3)
print(remaining)
remaining = slices_left(remaining, 2)
print(remaining)
