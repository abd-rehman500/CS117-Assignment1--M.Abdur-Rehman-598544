"""
Take the voltage V and resistance R from the user and calculate the current I=V/R.
If the current is more than 2 A, print "Fuse will blow"; otherwise print "Circuit is safe".
if R is zero or negative, print "Invalid resistance" instead.
"""

V = float(input("Enter the voltage (V): "))
R = float(input("Enter the resistance (R): "))

if R <= 0:
    print("Invalid resistance")
else:
    I = V / R
    print(f"Current = {I}")
    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
