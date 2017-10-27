import sys
import getopt
import os


def getArgs():
	try: 
		opts, args = getopt.getopt(sys.argv[1:],"f:h:w:",['help'])
	except getopt.GetoptError as e:
		print (str(e))
		print("Usage: %s " % sys.argv[0])
		sys.exit(2)
	file=''
	h=20
	w=20
	for o, a in opts:
		if o=='--help' :
			help()
		if o == '-f':
		   	file=a
		if o == '-h':
		    h=a
		if o =='-w':
			w=a


	return file,h,w


def errorFileArgNotFound():
	fileargnotfound=['Error no file argument found!','Please provide filename using \'-f <filename>\'.']
	fileError(fileargnotfound)

def errorFileNotFound():
	filenotfound=['File not found!','Please provide the correct using filename with path.']
	fileError(filenotfound)

def fileError(filenotfound):
	r, c = os.popen('stty size', 'r').read().split()
	r=int(r)
	c=int(c)
	print(r,c)
	print(int(c)*"*")
	for e in filenotfound:
		sp=int((c-len(e))/2)-1
		print(sp*" ",e,sp*" ")
	print(int(c)*"*")
	exit(0)

def help():
	print('helping...')
	exit(0)
