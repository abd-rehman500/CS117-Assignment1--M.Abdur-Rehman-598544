# Write a function star_to_delta(ra, rb, rc) that takes three resistance values from a Star (Y) network
# converts them to the equivalent Delta (Δ) network.
# The function must calculate the numerator factor first to avoid redundant calculations, using the formula:
# R_numerator= RaRb + RbRc + RcRa
# Then calculate the three Delta resistors:
# Rab=R_numerator/Rc,
# Rbc=R_numerator/Ra,
# Rca=R_numerator/Rb.
# Return the three newly calculated resistance values rounded to two decimal places.

def star_to_delta(ra,rb,rc):

    R_numerator = (ra*rb) + (rb*rc) + (rc*ra)

    rab = round((R_numerator/rc),2)
    rbc = round((R_numerator/ra),2)
    rca= round((R_numerator/rb),2)
    

    return (rab , rbc , rca)

print(star_to_delta(10, 20, 30))





