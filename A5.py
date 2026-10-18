# Take three resistor values from the user and display the smallest and the largest of them.
# Use only if/elif/else (no min() or max()).

R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))

if (R1 <= R2) and (R1 <= R3):
    smallest = R1
elif (R2 <= R1) and (R2 <= R3):
    smallest = R2
else:
    smallest = R3

if (R1 >= R2) and (R1 >= R3):
    largest = R1
elif (R2 >= R1) and (R2 >= R3):
    largest = R2
else:
    largest = R3

print(f"Smallest = {smallest} ohm ")
print(f"Largest = {largest} ohm ")