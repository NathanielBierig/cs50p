def main():
    word = input("Input: ")
    shorten(word)
def shorten(word):

    wrd =""
    for x in word:
        if x not in ["a","A", "e","E", "i", "I", "o", "O", "u", "U"]:
            wrd += x
    print (wrd)
    return wrd

if __name__ == "__main__":
    main()