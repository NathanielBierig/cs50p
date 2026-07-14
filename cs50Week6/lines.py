import sys
from pathlib import Path

p_root = str(Path(__file__).resolve().parent.parent)
# Put in week num space filename
if len(sys.argv) != 3: sys.exit("invalid arguments, use week num + filename")
else: p_root = p_root +"\cs50Week" + sys.argv[1] +"\\" + sys.argv[2]
count = 0
flag = False
with open(p_root) as file:
    for line in file:
        line = line.strip()
        if line.startswith("\"\"\""):
            flag = True 
        if line.endswith("\"\"\""):
            flag = False
            continue
        if line.startswith("#") or not line or flag:
            continue
        else: count += 1
print(f"{count} lines in file {sys.argv[2]} in project week {sys.argv[1]}")





