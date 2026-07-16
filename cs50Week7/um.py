import re

def main():
    print(count(input("Text: ")))

def count(s):
    # new thing i learned \b is boundry, to find word, would have been nice for youtube link
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()