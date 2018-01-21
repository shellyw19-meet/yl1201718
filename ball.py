from turtle import *
import random
 
colormode(255)

class Ball(Turtle):
 	def __init__(self,x,y,dx,dy,r):
 		turtle.__init__(self)
 		self.x = xcor()
 		self.y = ycor()
 		self.dx = dx
 		self.dy = dy
 		self.r = r
 		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))

 		self.shape("circle")
 		self.shapesize(r/10)

 	def move(self, screen_width, screen_hight):
 		current_x = self.xcor()
 		new_x = current_x + dx
		
 		current_y = self.ycor()
 		new_x = current_x + dx

 		right_side_ball = new_x + self.r
 		left_ball = new_x - r
 		top_side_ball = new_y + r
 		down_side_ball = new_y - r

 		self.goto(new_x, new_y)

 		if right_side_ball > screen_width:
 			new_x = current_x - self.dx*1
 		if left_side_ball < -screen_width:
 			new_x = current_x + self.dx*1
 		if up_side_ball > screen_hight:
 			new_y = current_y - self.dy*1
 		if down_side_ball < -screen_hight:
 			new_y = current_y + self.dy*1



