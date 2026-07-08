def main():
    tx = convert(input().strip())
    print(tx)


def convert(t):
    
    t = t.replace(":)", "🙂")
    t = t.replace(":(", "🙁")
    return t

main()