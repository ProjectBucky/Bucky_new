import re

query="sum of 2 and 3"

#for sum/diff/prod/quo of x and y
searchObj = re.search( r'(.*) of (.*) and (.*)', query, re.M|re.I)
if searchObj:	
	print ("searchObj.group() : ", searchObj.group())
	print ("searchObj.group(1) : ", searchObj.group(1))
	print ("searchObj.group(2) : ", searchObj.group(2))
	print ("searchObj.group(3) : ", searchObj.group(3))
	print(float(searchObj.group(2))+float(searchObj.group(3)))
