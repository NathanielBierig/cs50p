import sys
import csv

#read file line by line, split, write as first,last,house
if len(sys.argv) != 3: sys.exit("invalid arguments, need before and after file")

before = sys.argv[1]
after = sys.argv[2]
try: 
    with open(before) as infile, open(after, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        temp = {
        "first": "",
        "last": "",
        "house": ""
    }
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in reader:
            temp["last"],temp["first"] = line["name"].split(", ")
            temp["house"] = line["house"]
            writer.writerow(temp)
except FileNotFoundError:
    sys.exit("invalid before file")
except IndexError:
    sys.exit("File not formated correctly")

