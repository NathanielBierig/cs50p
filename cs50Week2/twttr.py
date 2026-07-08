word = input("Input: ")
wrd =""
for x in word:
    if x not in ["a","A", "e","E", "i", "I", "o", "O", "u", "U"]:
        wrd += x
print("Output: "+ wrd)