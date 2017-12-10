from turtle import *


class Rectangle(Turtle):
	def __init__(self,x,y,hight,width,color):
		self.color = color
		self.x = xcor()
		self.y = ycor()
		Turtle.__init__(self)
		register_shape("rectangle", ((int(width),0),(int(width),int(hight)),(0,int(hight)),(0,0)))

rec1 = Rectangle(100,200,10,20,"green")
rec2 = Rectangle(50,0,10,20,"red")

mainloop()