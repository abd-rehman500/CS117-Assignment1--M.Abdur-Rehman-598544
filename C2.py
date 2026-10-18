#Write a function parallel_resistance(resistors) that takes a list of resistor values 
# and returns the equivalent resistance of the parallel combination: 1 / R_eq = 1/R1 + 1/R2 + ...

def parallel_resistence(resistors):

    resi = 0
    for resistor in resistors:

        resi += (1/resistor)
        R_eq = round((1/resi),2)
    return R_eq


print(parallel_resistence([10, 10]))

print(parallel_resistence([100 , 300 , 200]))
