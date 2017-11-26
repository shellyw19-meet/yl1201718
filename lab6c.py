from turtle import *

class hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.begin_poly()
		for i in range(0,6):
			self.forward(size)
			self.left(60)
		self.end_poly()
		register_shape("hexagon",self.get_poly())
		self.shape("hexagon")	

hex1 = hexagon(150)
print(hex1)

mainloop()
