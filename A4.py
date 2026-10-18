"""
Take two bits A and B from the user and print the output of the AND, OR and XOR gates
If either input is not 0 or 1, print "Bits must be 0 or 1". 
"""

A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A not in [0, 1] or B not in [0, 1]:
    print("Bits must be 0 or 1")
else:

    if A == 1 and B ==1:
        and_out = 1
    else:
        and_out = 0

    if A == 1 or B == 1:
        or_out = 1
    else:
        or_out = 0

    if A != B:
        xor = 1
    else:
        xor = 0

print(f"AND = {and_out}")
print(f"OR = {or_out}")
print(f"XOR = {xor}")

