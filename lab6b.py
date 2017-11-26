from turtle import *

import random

colormode(255)

class Rectangle(Turtle):
	def __init__(self,hight,width):
		Turtle.__init__(self)
		register_shape("rectangle", ((int(width),0),(int(width),int(hight)),(0,int(hight)),(0,0)))
		
		self.shape("rectangle")
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))

class Square(Rectangle):
	def __init__(self,hight):
		Rectangle.__init__(self,hight,hight)

rect1 = Square(200)
rect1.random_color()
print(rect1)

mainloop()

