from turtle import *
import turtle
import random
import time
import math
from ball import Ball
tracer(0)
hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,10,10,8)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
	dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))	
	r = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))

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

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				ball_a_r = ball_a.r
				ball_b_r = ball_b.r

				new_ball_x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				new_ball_y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				new_ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
				while new_ball_dx == 0:
					new_ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
				new_ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
				while  new_ball_dy == 0:
					new_ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
				new_ball_r = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
				new_ball_color = ((random.random(),random.random(),random.random()))

		if ball_a.r < ball_b.r:
			ball_a.goto(x,y)
			ball_a.dx = new_ball_dx
			ball_a.dy = new_ball_dy
			new_ball.r = new_ball_r
			new_ball.color = new_ball_color

			ball_a.shapesize(new_ball.r/10)

			ball_b.r = ball_b.r + 1
			ball_b.shapesize(ball_b.r/10)

		if ball_b.r < ball_a.r:
			ball_b.goto(x,y)
			ball_b.dx = new_ball_dx
			ball_b.dy = new_ball_dy
			new_ball.r = new_ball_r
			new_ball.color = new_ball_color

			ball_b.shapesize(new_ball.r/10)

			ball_a.r = ball_a.r + 1
			ball_a.shapesize(ball_a.r/10)

def check_myball_collision():
	for 




















