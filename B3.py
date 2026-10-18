# A sensor gave these voltage readings:
# readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2). 
# Using one loop (no max(), min() or sum()), find and print:
# (a) how many readings are above 3.2 V, 
# (b) the highest reading,
# (c) the lowest reading,
# (d) the average reading.

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above_3_2 = 0
highest = readings[0]
lowest = readings[0]
total = 0

for reading in readings:
    if reading > 3.2:
        above_3_2 += 1
    if reading > highest:
        highest = reading
    if reading < lowest:
        lowest = reading
    total += reading

average = round(total / len(readings),2)

print(f"Readings above 3.2 V: {above_3_2}")
print(f"Highest: {highest} V")
print(f"Lowest: {lowest} V")
print(f"Average: {average} V")

