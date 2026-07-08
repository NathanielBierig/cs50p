import inflect
p = inflect.engine()
l = []
try:
   
    while 1:
        name = input("Name: ")
        l.append(name)

except EOFError:
    print("Adieu, adieu, to ", p.join(l))

