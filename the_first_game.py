import turtle
windo = turtle.Screen()
windo.title("ping pong By Codzilla")
windo.bgcolor("black")
windo.setup(width=800, height=600)
windo.tracer(0)

#midrab 1
midrab1 = turtle.Turtle()
midrab1.speed(0)
midrab1.shape("square")
midrab1.color("blue")
midrab1.shapesize(stretch_wid=5,stretch_len=1)
midrab1.penup()
midrab1.goto(-350,0)

#misrab 2
misrab2=turtle.Turtle()
misrab2.speed(0)
misrab2.shape("square")
misrab2.color("red")
misrab2.shapesize(stretch_wid=5,stretch_len=1)
misrab2.penup()
misrab2.goto(350,0)
#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx =1.5
ball.dy= 1.5



#functions
def misrab1_Up():
    y=midrab1.ycor()
    y += 25
    midrab1.sety(y)
def misrab1_Down():
    y = midrab1.ycor() 
    y-= 25
    midrab1.sety(y)
def misrab2_Up():
    y = misrab2.ycor()
    y+= 25
    misrab2.sety(y)
def misrab2_Down():
    y=misrab2.ycor()
    y-= 25
    misrab2.sety(y)
#
windo.listen()
windo.onkeypress(misrab1_Up, "w")
windo.onkeypress(misrab1_Down, "s")
windo.onkeypress(misrab2_Up, "Up")
windo.onkeypress(misrab2_Down, "Down")
while True:
    windo.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1   

    if  ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if  ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1    



    if (ball.xcor() >340 and ball.xcor() < 350)and(ball.ycor() < misrab2.ycor()+40 and ball.ycor() > misrab2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350)and(ball.ycor() < midrab1.ycor()+40 and ball.ycor() >midrab1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1    