#Sandwich Shop Cost
##A copy of Rickey Glover's Sandwhich Shop Discount Calculator rewritten in Python

print ('This is a program to calculate the discount rate in a sandwhich shop\n')

sandwich_size = str(input("What size sandwich would you like? Regular or Large:"))
discount = int(input("What is your age?"))

regular_price = 5.45
large_price = 8.95

student_discount = 0.10
senior_discount = 0.20

if sandwich_size == "regular" or sandwich_size == "Regular" or sandwich_size == "REGULAR":
    if discount <= 17:
        final_price = regular_price - (regular_price * student_discount)
    elif discount >= 65:
        final_price = regular_price - (regular_price * senior_discount)
    else:
        final_price = regular_price
elif sandwich_size == "large" or sandwich_size == "Large" or sandwich_size == "LARGE":
    if discount <= 17:
        final_price = large_price - (large_price * student_discount)
    elif discount >= 65:
        final_price = large_price - (large_price * senior_discount)
    else:
        final_price = large_price

rounded_final = round(final_price, 2)

print ("The final price of your order will be ${}!".format(rounded_final))