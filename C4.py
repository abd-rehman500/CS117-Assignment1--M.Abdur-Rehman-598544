# The standard voltage divider formula assumes no current is drawn by the load, which is rarely true in practical circuits.
# Write a function loaded_divider(vs, r1, r2, rl) that calculates the true output voltage when a load resistor rl is attached in parallel with r2.
# The function must first compute the parallel equivalent of r2 and rl, then apply the voltage divider formula with vs and r1.
# Return both the unloaded theoretical voltage and the actual loaded voltage

def loaded_divider(vs,r1,r2,rl):

    # as rl and r2 in parallel , we'll find the req for them first called R_eq_par
    R_eq_par = ((1/rl) + (1/r2))
    R_eq_par = round((1/R_eq_par),2)

    # R_total will be the total resistence experienced by the circuit
    R_total = R_eq_par + r1

    # The unloaded voltage across r2 is given by the voltage divider formula
    V_unloaded = round((vs * (r2 / (r1 + r2))),2)

    # The loaded voltage across the parallel combination is given by the voltage divider formula
    V_loaded = round((vs * (R_eq_par / (r1 + R_eq_par))),2)

    return V_unloaded, V_loaded

print(loaded_divider(12, 1000, 1000, 500))