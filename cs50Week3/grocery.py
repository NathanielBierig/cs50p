try:
    glist = set()
    while 1:
        glist.add(input())

except EOFError:
    count = 1
    for x in glist:
        print(str(count), " ", x.upper() )
        count += 1

