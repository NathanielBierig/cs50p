import re
import sys

# This one was hard, felt like whack a mole with errors. enjoyed
def main():
    print("input x AM to y PM")
    print(convert(input("Hours: ")))

        
def convert(s):
    pattern = r"^((?:1[0-2]|[1-9])(?::[0-5][0-9])?) ((?:A|P)M) to ((?:1[0-2]|[1-9])(?::[0-5][0-9])?) ((?:A|P)M)$"
    match = re.search(pattern, s)
    if not bool(match): raise ValueError # if invalid raise error
    #convert 1,2
    first, second = "", ""
    #group 1
    hour = int(match.group(1).split(":")[0])
    if hour == 12:
        hour = 0
    if match.group(2) == "AM":
      
       
       if ":" in match.group(1):
            first = f"{hour:02}:{match.group(1).split(':')[1]}"
       else:
            first = f"{hour:02}:00"
    else:
       
        hour = str(int(hour)+12)
        if ":" in match.group(1):
            first = f"{hour:02}:{match.group(1).split(':')[1]}"
        else:
            first = f"{hour:02}:00"
            # group 2
    hour = int(match.group(3).split(":")[0])
    if hour == 12:
            hour = 0
    if match.group(4) == "AM":
       
       
       if ":" in match.group(1):
            second = f"{hour:02}:{match.group(3).split(':')[1]}"
       else:
            second = f"{hour:02}:00"
    else:
        
        hour = hour + 12
        if ":" in match.group(3):
            second = f"{hour:02}:{match.group(3).split(':')[1]}"
        else:
            second = f"{hour:02}:00"
    return f"{first} to {second}"






if __name__ == "__main__":
    main()