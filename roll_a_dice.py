import random
def roll_a_dice():
	face=range(1,7)
	choice = random.choice(face)
	numstr = ["one","two","three","four","five","six","seven","eight"]
	return "Dice rolled and Its "+str(numstr[face.index(choice)])