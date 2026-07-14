import sys
from pathlib import Path
import csv
from tabulate import tabulate

if len(sys.argv) != 2: sys.exit("invalid argument must input file name")

### use regular.csv and sicilian.csv
# not needed just put the aarg in directly 
# path = str(Path(__file__).resolve().parent) +"\\"+ sys.argv[1]

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")

