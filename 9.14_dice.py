from random import randint

class Die():
	def __init__(self,sides):
		self.sides=sides
		
	def roll_die(self):
		print(randint(1,self.sides))
		
die1=Die(10)
x=0
while x<10:
	die1.roll_die()
	x+=1

print("===============================================")
		
die2=Die(20)
x=0
while x<10:
	die2.roll_die()
	x+=1
