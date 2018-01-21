from turtle import *
import turtle
import random
import time
import math
from ball import *

turtle.tracer(0)
turtle.hideturtle()

RUNNING = true
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = ball(0,0,10,10,8)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range():
	x = random.randit(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randit(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randit(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
	dy = random.randit(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))	
	r = random.randit(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))

	Ball1 = Ball(x,y,dx,dy,r)
	BALLS.append(Ball1)

def move_all_balls():
	for h in BALLS:
		h.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

	D = math.sqrt(math.pow((ball_2.xcor()-ball_1.xcor()),2)+math.pow((ball_2.ycor(-ball_1.ycor()),2)))

	if D < ball_b.r + ball_a.r:
		return True
	else: 
		return False