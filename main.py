# import cv2
import sys
from PIL import Image
from color import *
import scipy.misc as sm
from util import getArgs,errorFileNotFound,help,errorFileArgNotFound

cv=False;
#add support for cv2
def usePIL(file,size):
	try:
		img=Image.open(file)
	except IOError:
		errorFileNotFound()

	img = np.array(Image.open(file))
	img = sm.imresize(img,size)
	l=img.shape
	return img

def useCV2(file,size):
	global cv
	cv=True 
	try:
		img=cv2.imread(file)
	except IOError:
		errorFileNotFound()
	img=cv2.resize(img, size)
	return img

file,h,w=getArgs()
size=(int(h),int(w))
# check if cv2 is available
try:
	import cv2
	img=useCV2(file,size)
except ImportError:
	img=usePIL(file,size)


# exit(0);

if not file:
	errorFileArgNotFound()
print(file,size)

print(img[1,2])
# exit(0)
for i in range(0,size[0]):
	for j in range(0,size[1]):
		code=str(output(rgb(img[i][j])))
		sys.stdout.write("\u001b[38;5;"+code+"m  \033[;7m")
	print(u"\u001b[42;1m")




