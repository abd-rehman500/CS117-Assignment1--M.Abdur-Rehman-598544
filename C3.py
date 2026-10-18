#Write a function decimal_to_binary(n) that converts a positive decimal number to a binary string
# using repeated division by 2 (do not use bin()).

def decimal_to_binary(number):

    binary = ""
    if number != 0:
        while number > 0:   
            remainder = str(number % 2)
            binary = remainder + binary
            number = (number //2)
        return binary
    else:
        return ("0")

print(decimal_to_binary(10))
print(decimal_to_binary(25))


    

