# import cv2
import sys
from PIL import Image
from color import *
import scipy.misc as sm
import getopt
import os
# img = cv2.imread('flag.jpg')


# size = (20, 40)
try:
    myopts, args = getopt.getopt(sys.argv[1:],"f:h:w:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s " % sys.argv[0])
    sys.exit(2)
file=''
h=50
w=50
for o, a in myopts:
    if o == '-f':
        file=a
    elif o == '-h':
        h=a
    elif o=='-w':
    	w=a

r, c = os.popen('stty size', 'r').read().split()
r=int(r)
c=int(c)
print(r,c)
filenotfound=' \n Please provide filename using -f <filename>!!'
if not file:
	print(int(c)*"*")
	e1='Error no file argument found!'
	sp=int((c-len(e1))/2)
	print('*',sp*" ",e1)
	e1="Please provide filename using -f <filename>!!"
	sp=sp=int((c-len(e1))/2)
	print('*',sp*" ",e1)
	print(int(c)*"*")
	exit(0)

size=(h,w)
print(file,size)
exit(0)

img = np.array(Image.open(file))
img = sm.imresize(img,size)
# img=cv2.resize(img, (400, 200)) 
# img = cv2.GaussianBlur(img,(5,5),0)
# ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
l=img.shape
# print(img[0][0])
for i in range(0,l[0]):
	for j in range(0,l[1]):
		code=str(output(img[i][j]))
		sys.stdout.write("\u001b[38;5;"+code+"m \033[;7m")
	print(u"\u001b[42;1m")




# cv2.imshow('image', img)
# cv2.waitKey()
