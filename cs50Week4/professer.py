import random


def main():
    global lvl
    try:
        
        lvl = int(input("Level: "))
        if lvl not in [ 1, 2 , 3]: raise ValueError
    except ValueError:
        print("invalid level.")
    score = 0
    equations = generate_problems(get_level())
    score = answers(equations)
    print("Score: " + str(score))
    

def get_level():
    return lvl
def generate_integers(level):
    mn = 10 ** (level -1)
    mx = 10 ** level - 1
    return random.randint(mn,mx)

def generate_problems(level):
    problems = []
      
    for x in range(10):
        problems.append([generate_integers(level), generate_integers(level)])
    return problems

def answers(probs):
    score = 0
    for x, y in probs:
        first_try = 1
        while 1:
            ans = int(input(f"{x} + {y} = "))
            if ans != x + y:
                first_try = 0
                print("EEE")
            else:
                if first_try: 
                    score += 1
                break
    return score
        




if __name__ == "__main__":
    main()