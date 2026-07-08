### for letter in string if capital add _ and letter
camel = input("camelCase: ").strip()
snake = camel[0].lower()
for c in camel[1:]:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake+= c
print("Snake Case: "+ snake)
