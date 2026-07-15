import sys
from PIL import Image, ImageOps

# python .\shirt.py before1.jpg, files in folder muppets in cs50Week6 folder, called before 1-3 . jpg
#input before1.jpg or something
if len(sys.argv) != 2: sys.exit("invalid argument must input file name")
try:
    imgfile = "muppets\\" + sys.argv[1]
    shirt = Image.open("shirt.png") #open images
    selfie = Image.open(imgfile)

    selfie = ImageOps.fit(selfie, shirt.size) #resize

    selfie.paste(shirt, (0, 0), shirt) #add shirt
    selfie.save(f"muppets_with_shirt\\{sys.argv[1][:-4]}withshirt.jpg") #save file

except FileNotFoundError:
    sys.exit("File not found")

