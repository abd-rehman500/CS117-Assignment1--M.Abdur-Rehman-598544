# Write two functions:
#  ohms_current(v, r) that returns the current I = V / R, and power_dissipated(i, r) that returns the power P = I² × R.
#  Test them for V = 12 V and R = 6 ohm.

def ohms_current(v,r):
    return v/r

def power_dissipated(i,r):
    return ((i**2)*r)

# test
V = 12
R = 6
I = ohms_current(V,R)
P = power_dissipated(I,R)

print(f"Current = {I} A")
print(f"Power = {P} W")
