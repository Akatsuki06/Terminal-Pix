# import cv2
import sys
from PIL import Image
from color import *
import scipy.misc as sm

# img = cv2.imread('flag.jpg')

file = 'flag.jpg'
size = (40,50)
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
