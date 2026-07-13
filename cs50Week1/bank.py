def main():
    word = input("Input: ")
    value(word)

def value(greeting):
    #greeting = input("Greeting: ").strip().lower()
    greeting = greeting.strip().lower()
    if greeting == "hello": 
        print("0")
        return 0
    elif greeting[0] == ("h"):
        print("20")
        return 20
    else :
        print("100")
        return 100



if __name__ == "__main__":
    main()