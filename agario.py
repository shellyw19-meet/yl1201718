import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.ht()

# These all are global needed variables
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2 # here we get the canvas(screen) height

# MY_BALL related
INIT_MYBALL_X = 0
INIT_MYBALL_Y = 21
INIT_MYBALL_DX = 0
INIT_MYBALL_DY = 0
INIT_MYBALL_RADIUS = 50
INIT_MYBALL_COLOR = 'blue'

# BALLS related
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

# creating MY_BALL
MY_BALL = Ball(INIT_MYBALL_X,INIT_MYBALL_Y,INIT_MYBALL_DX,INIT_MYBALL_DY,INIT_MYBALL_RADIUS)

# creating BALLS (it will store all balls created)
BALLS = []

# This loop prepares the list BALLS
for i in range(NUMBER_OF_BALLS):
	init_ball_x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	init_ball_y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	init_ball_dx = random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	init_ball_dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	while (init_ball_dx == 0):
		init_ball_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while (init_ball_dy == 0):
		init_ball_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	init_ball_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	new_ball = Ball(init_ball_x, init_ball_y, init_ball_dx, init_ball_dy, init_ball_radius)
	BALLS.append(new_ball)



def move_all_balls():
	for new_ball in BALLS:
		new_ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)



def collide(ball_a, ball_b):
	if(ball_a == ball_b):
		return False
	ball_a_x = ball_a.xcor()
	ball_a_y = ball_a.ycor()
	ball_a_r = ball_a.r

	ball_b_x = ball_b.xcor()
	ball_b_y = ball_b.ycor()
	ball_b_r = ball_b.r

	D = ((ball_a_x - ball_b_x)**2+(ball_a_y - ball_b_y)**2)**0.5
	sr = ball_a_r + ball_b_r

	if(D + 10<= sr):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			# if collide(ball_a,ball_b):
			# 	ball_a_r = ball_a.r
			# 	ball_b_r = ball_b.r

				new_ball_x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				new_ball_y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))

				new_ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
				new_ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				while new_ball_dx == 0:
					new_ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
					new_ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
				while  new_ball_dy == 0:
					new_ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
					new_ball_r = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
					new_ball_color = ((random.random(),random.random(),random.random()))
				if collide(ball_a,ball_b)==True:
					ball_a_r = ball_a.r
					ball_b_r = ball_b.r
					if ball_a.r < ball_b.r:
						ball_a.goto(new_ball_x,new_ball_y)
						ball_a_dx = new_ball.dx
						ball_a_dy = new_ball.dy
						ball_a_r = new_ball.r
						ball_a_color = new_ball.color

						ball_a.shapesize(new_ball.r/10)

						ball_b.r = ball_b.r + 1
						ball_b.shapesize(ball_b.r/10)

					if ball_b.r < ball_a.r:
						ball_b.goto(new_ball_x,new_ball_y)
						ball_b_dx = new_ball.dx
						ball_b_dy = new_ball.dy
						ball_b_r = new_ball.r
						ball_b_color = new_ball.color

						ball_b.shapesize(new_ball.r/10)

						ball_a.r = ball_a.r + 1
						ball_a.shapesize(ball_a.r/10)

def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL, ball):
			ball_radius = ball.r
			my_ball_radius = MY_BALL.r
			
			if ball_radius > my_ball_radius:
				return False

			else:
			
				ball_dx = new_ball.dx
				ball_dy = new_ball.dy
				ball_r = new_ball.r
				ball_color = new_ball.color

				MY_BALL.r = MY_BALL.r + 1

	return True

def movearound(event):
	MY_BALL.goto(event.x, event.y)
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.listen()
# for i in range(40000):
# 	move_all_balls()
# 	getscreen().update()

while RUNNING == True:
	if SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 or SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_HEIGHT,SCREEN_HEIGHT)
	RUNNING = check_myball_collision()

time.sleep(SLEEP)

turtle.getscreen().update()	
turtle.mainloop()
