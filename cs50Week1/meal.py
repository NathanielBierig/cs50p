
def main():
    print(convert(input("What time is it?: ").split(":")))

def convert(time):
    if time[1][-2:].lower() == "am":
        if time[0] == "7" or time == ["8", "00 am"]:
            return ("breakfast time")
    elif time[1][-2:].lower() == "pm":
        if time[0] == "12" or time == ["1", "00 pm"]:
            return ("lunch time")
        elif time[0] == "6" or time == ["7", "00 pm"]:
            return ("dinner time")
    else:
        if time[0] == "7" or time == ["8", "00"]: 
            return ("breakfast time")
        elif time[0] == "12" or time == ["13", "00"]:
            return ("lunch time")
        elif time[0] == "18" or time == ["19", "00"]:
            return ("dinner time")       
    return ""
# doesnt check for trailing stuff as in 12:00 m or 12:00 dndbihd will return lunch time


if __name__ == "__main__":
    main()