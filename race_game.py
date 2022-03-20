import turtle
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Track border left
borderLeft = turtle.Turtle()
borderLeft.speed(0)
borderLeft.shape("square")
borderLeft.color("white")
borderLeft.shapesize(stretch_wid=30,stretch_len=.5)
borderLeft.penup()
borderLeft.goto(-200, 0)

# Track border right
borderRight = turtle.Turtle()
borderRight.speed(0)
borderRight.shape("square")
borderRight.color("white")
borderRight.shapesize(stretch_wid=30,stretch_len=.5)
borderRight.penup()
borderRight.goto(200, 0)

# Car
car = turtle.Turtle()
car.speed(0)
car.shape("square")
car.color("white")
car.shapesize(stretch_wid=3,stretch_len=2)
car.penup()
car.color("red")
car.goto(0, -240)

# # Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-400, 250)
pen.write("Score: 0", align="Left", font=("Courier", 24, "normal"))


# Main game loop
while True:
	wn.update()
	 	