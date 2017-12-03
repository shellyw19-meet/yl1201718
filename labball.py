from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
		self.radius=radius

ball1 = Ball(15,"green", 15)
ball2 = Ball(10,"yellow", 7)

# print(ball1.shapesize())
# def Distance(x1, x2, y1, y2):
# 	distance = math.sqrt((math.pow(ball2.xcor()-ball1.xcor(),2) + math.pow(ball2.ycor()-ball1.ycor(),2)))

def check_collision(ball1, ball2):
	if ball1.shapesize() + ball2.shapesize() > math.sqrt((math.pow(ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))

	print ("the balls are collising")


check_collision(ball1,ball2)
mainloop()