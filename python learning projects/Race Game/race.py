import turtle
import random
import keyboard

win = turtle.Screen()
win.bgcolor("white")
win.screensize(1000, 600)
win.tracer(0)

racer1 = turtle.Turtle()
racer1.shape("triangle")
racer1.left(90)
racer1.penup()
racer1.goto(0-20, -250)
racer1.speed(0)

racer2 = turtle.Turtle()
racer2.shape("triangle")
racer2.left(90)
racer2.penup()
racer2.goto(20, -250)
racer2.speed(0)


def racer1key():
  win.tracer(1)
  racer1.pendown()
  racer1.speed(random.randint(1, 10))
  racer1.forward(random.randint(10, 200))

def racer2key():
  win.tracer(1)
  racer2.pendown()
  racer2.speed(random.randint(1, 10))
  racer2.forward(random.randint(10, 200))

win.listen()
win.onkeypress(racer1key, "w")
win.onkeypress(racer2key, "Up")

#Main Game Loop
while True:
  win.update()
