from PIL import Image
import sys

location = str(sys.argv[1])

basewidth = 320
img = Image.open(location)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save(location)
