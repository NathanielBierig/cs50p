def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) < 2 or len(s) > 6): return False
    elif  s[:2].isalpha() == False: return False
    elif  s.isalnum() == False: return False
    flag = 0
    for x in s:
        if x.isdigit(): flag = 1
        if flag and x.isalpha(): return False
    else: return True


main()