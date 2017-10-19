# https://jonasjacek.github.io/colors/data.json
import json

def fetchdata():
	with open('data.json') as data_file:
		data=json.load(data_file)
	return data

def getColorList():
	data=fetchdata()
	colorList=[];
	for i in data:
		# n=['colorId']
		r=i['rgb']['r']
		g=i['rgb']['g']
		b=i['rgb']['b']
		colorList.append([r,g,b])
	return colorList