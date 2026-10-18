"""
Take a current value from the user. If it is positive, print "Current flows from A to B".
If it is negative, print "Current flows from B to A".
If it is zero, print "No current flows".
"""

Current = float(input("Enter the current value: "))
if Current == 0:
    print("No current flows")
else:
    if Current > 0:
        print("Current flows from A to B")
    else:
        print("Current flows from B to A")
