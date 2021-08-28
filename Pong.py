import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black") # background color
wn.setup(width=800, height=600)
wn.tracer(0) # stops the window from updating

#Score 
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # turtle object
paddle_a.speed(0) # speed of animation, maximum possible speed
paddle_a.shape("square") # default = 20px x 20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretch width by 5 = 20x5 px
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle() # turtle object
paddle_b.speed(0) # speed of animation, maximum possible speed
paddle_b.shape("square") # default = 20px x 20px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretch width by 5 = 20x5 px
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle() # turtle object
ball.speed(0) # speed of animation, maximum possible speed
ball.shape("square") # default = 20px x 20px
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = -4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() #.ycore from turtle module, returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # .ycore from turtle module, returns the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #.ycore from turtle module, returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # .ycore from turtle module, returns the y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse the direction
        os.system("afplay bounce.wav&") # & to avoid the game stop while reproducing the sound

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse the direction
        os.system("afplay bounce.wav&") # & to avoid the game stop while reproducing the sound

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 # reverse the direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1 # reverse the direction
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Collision between paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&") # & to avoid the game stop while reproducing the sound

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&") # & to avoid the game stop while reproducing the sound