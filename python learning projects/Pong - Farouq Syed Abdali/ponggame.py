#Beginner Pong game tutorial
#By: Farouq Syed Abdali

import turtle
import winsound


#Screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Pong by Farouq Syed Abdali")
win.setup(width=800, height=600)
win.tracer(0)

#Score Count
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8
ball.dy = -0.8

#Text
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Author Text
author = turtle.Turtle()
author.speed(0)
author.color("white")
author.penup()
author.hideturtle()
author.goto(0, -280)
author.write("Made by: Farouq Syed Abdali", align="center", font=("Courier", 18, "bold"))

#Paddle Movement
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)


#Key Binds
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
  win.update()

  #Ball Movement
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  #Screen Border Bounce
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

  #Paddle and Ball Collisions
  if (ball.xcor() > 340 and ball.ycor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
  
  if (ball.xcor() < -340 and ball.ycor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1
