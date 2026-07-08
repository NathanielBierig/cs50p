menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
try:
    total = 0.0
    while 1:
        item = input("Item: ")
        total += menu[item]
        print(f"Total: $ {total:.2f} \n")








except EOFError:
    print("enjoy your tacos, have a good day.")
except KeyError:
    print("not on the menu :(")