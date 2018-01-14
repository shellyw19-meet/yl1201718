from turtle import *
import random
 

class Ball(Turtle):
 	def __init__(self,x,y,dx,dy,r,color):
 		turtle.__init__(self)
 		self.x = xcor()
 		self.y = ycor()
 		self.dx = dx
 		self.dy = dy
 		self.r = r
 		
 		self.color(color)
 		self.shape("circle")
 		self.shapesize(r/10)

 	def move(self, screen_width, screen_hight):
 		current_x = xcor()
 		new_x = corrent_x + dx
		
 		current_y = ycor()
 		new_x = corrent_x + dx

 		right_side_ball = new_x + r
 		left_ball = new_x - r
 		top_side_ball = new_y + r
 		down_side_ball = new_y - r

 		self.goto(new_x, new_y)

 		if right_side_ball > screen_width



