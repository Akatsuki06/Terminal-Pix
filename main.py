# import cv2
import sys
from PIL import Image
from color import *
import scipy.misc as sm
from util import getArgs,errorFileNotFound,help,errorFileArgNotFound

file,h,w=getArgs()
size=(int(h),int(w))

# file='flag.jpg'
if not file:
	errorFileArgNotFound()
print(file,size)
# exit(0)
try:
    img=Image.open(file)
    # do stuff
except IOError:
	print('')
	# errorFileNotFound()

img = np.array(Image.open(file))
img = sm.imresize(img,size)
l=img.shape
# print(img[0][0])
for i in range(0,l[0]):
	for j in range(0,l[1]):
		code=str(output(img[i][j]))
		sys.stdout.write("\u001b[38;5;"+code+"m  \033[;7m")
	print(u"\u001b[42;1m")




# cv2.imshow('image', img)
# cv2.waitKey()

