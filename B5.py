#You are testing a batch of manufactured 100-ohm resistors to bin them by tolerance. 
# Write a program with a while loop that continuously asks the user to input a measured resistance value.
# The loop should stop when the user enters 0. Sort the inputs into three running counts:
#•	1% tolerance (99.0 to 101.0 ohms)
#•	5% tolerance (95.0 to 105.0 ohms, excluding those that qualify for 1%)
#•	Reject (outside 95.0 to 105.0 ohms) Print the final count of resistors in each bin once the loop terminates.

one_percent = 0
five_percent = 0
reject = 0

while True:
    resistance = float(input("Enter the resistance value: "))
    if resistance != 0:
        if ( 99.0 <= resistance <= 101.0):
            one_percent += 1
        elif ( 95.0 <= resistance <= 105.0):
            five_percent += 1
        else:
            reject += 1
    else:
        break

print(f"Count of 1% tolerance resistors = {one_percent}")
print(f"Count of 5% tolerance resistors = {five_percent}")
print(f"Count of rejected resistors = {reject}")