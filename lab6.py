from turtle import *

import random

colormode(255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))

square1=Square(20)
square1.random_color()
print(square1)

mainloop()
