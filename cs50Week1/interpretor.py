xpression = input("Expression: ").split()
try:
    if xpression[1] not in ["+", "-", "x", "*", "/"]:
        raise ValueError
    float((float(xpression[0])+float(xpression[2])))
except ValueError:
    print("error not valid equation")
if xpression[1] == "+":
    print (float(xpression[0]) + float(xpression[2]))
elif xpression[1] == "-":
    print (float(xpression[0]) - float(xpression[2]))
elif xpression[1] == "/":
    if xpression[2]== "0":
        print("error devide by zero")    
    else:
        print (float(xpression[0]) / float(xpression[2]))
else:
    print (float(xpression[0]) * float(xpression[2]))


