amount_due = 50
print("A Coke costs 50 cents:\n")
while amount_due > 0:
    pay = int(input("insert coin: "))
    if pay not in [5,10,25]:
        print("invalid value try again")
        continue
    amount_due -= pay
    
    if amount_due <= 0:
        print("Change owed: "+str(abs(amount_due)))
    else:
        print("amount due: " + str(amount_due))