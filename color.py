import numpy as np
from colorinfo import *
def Black():
	print('\033[030m*\033[0m',end='')

def Red():
	print('\033[031m*\033[0m',end='')

def Green():
	print('\033[032m*\033[0m',end='')

def Yellow():
	print('\033[033m*\033[0m',end='')

def Blue():
	print('\033[034m*\033[0m',end='')

def Magenta():
	print('\033[035m*\033[0m',end='')

def Cyan():
	print('\033[036m*\033[0m',end='')

def White():
	print('\033[037m*\033[0m',end='')

def output(pixel):#RGB
	colorList=getColorList()
	nearest = min(colorList, key=lambda x: distance(x, pixel))
	ind=0;
	for i in colorList:
		if(i==nearest):break;
		ind=ind+1
	return ind


def distance(x,y): #eucledian formula
	r,g,b=x
	r1,g1,b1=y #similar to assigning value 
	return np.sqrt((r-r1)**2 + (g-g1)**2 +(b-b1)**2)

def rgb(bgr):
	return [bgr[2],bgr[1],bgr[0]]