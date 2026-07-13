# original code, focused on errors, try except etc
"""
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
"""
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x > y or x < 0 or y < 0:
        raise ValueError

    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


