import random
def roll_a_dice():
	face=range(1,7)
	choice = random.choice(face)
	numstr = ["one","two","three","four","five","six","seven","eight"]
	return "Dice rolled and Its "+str(numstr[face.index(choice)])
def roll_n_dice(num):
	face=range(1,7)
	choice = list()
	numstr = ["one","two","three","four","five","six","seven","eight"]
	for i in range(0,num):
		choice.append(random.choice(face))
	retstr = "Rolled "+str(num)+" dice, got "
	for i in range(0,len(choice)):
		retstr += str(numstr[face.index(choice[i])])
		if i==(len(choice)-2):
			retstr += " and "
		elif i!=(len(choice)-1):
			retstr += ", "
	return retstr
