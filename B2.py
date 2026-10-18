# Ask the user how many resistors are connected in series.
# Then use a loop to read the value of each resistor
# print the total series resistance (R_total = R1 + R2 + ...)

total_resistors = int(input("How many resistors? "))

R_total = 0

for i in range(0,total_resistors):
    resisitor = int(input(f"Enter R{i+1}: "))
    R_total += resisitor

print(f"Total resistance = {R_total} ohm")


