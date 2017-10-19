import cv2
import sys
from color import *
img = cv2.imread('flag.jpg')


img=cv2.resize(img, (100, 40)) 
# blur = cv2.GaussianBlur(img,(5,5),0)
# ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
l=img.shape
print(img[0][0])
for i in range(0,l[0]):
	for j in range(0,l[1]):
		code=str(output(img[i][j]))
		sys.stdout.write(u"\u001b[38;5;"+code+"m \033[;7m")
		# sys.stdout.write(' ')
		# print('\033[;7m',end='')	
	print(u"\u001b[42;1m")


for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        
    print(u"\u001b[0m")

cv2.imshow('image', img)
cv2.waitKey()
