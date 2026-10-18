# A resistor has a fixed value of 10 ohm. Using a for loop,
# print the current through it for supply voltages from 1 V to 10 V in steps of 1 V

R = 10

for v in range(1,11,1):
    current = (v/R)
    print(f"V = {v} V , I = {current} A")
