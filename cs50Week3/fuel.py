try:
    x, y = input("fraction: ").split("/")

    x = int(x)
    y = int(y)
    if not y: raise ZeroDivisionError
    if (y < x or x < 0 or y <= 0):
        raise ValueError
    




except ValueError:
    print("invalid fraction int value")
except ZeroDivisionError:
    print("zero as y value :(")
else:
    frac = int(100 * x/y)
    if frac <= 1: print("E")
    elif frac >= 99: print("F")
    else:
        print(f"%{frac}")



