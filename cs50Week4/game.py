import random

while 1:
    l = input("Level: ")
    if not l.isdigit():
        continue
    l = int(l)
    if l < 1:
        print("must input positive number try again")
    else:
        
        break
magic_Number = random.randint(1, l)
while 1: 
    i = input("Guess: ")
    if not i.isdigit():
        continue
    else:
        i = int(i)
    if  i == magic_Number:
        print("Just right!")
        break
    elif i < magic_Number:
        print("Too Low")
    else:
        print("Too High")
