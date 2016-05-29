import sys
import turtle

#circle
pond = turtle.Screen()
turtle.setup (2000, 1000, 0, 0)
pond.bgcolor("white")
head=turtle.Turtle()
head.up()
head.goto(0,0)
head.down()
head.color("red")
head.fillcolor("red")
head.begin_fill()

head.width(width=5)
turtle.fillcolor("green")
head.circle(40)
head.end_fill()

#line
line =turtle.Turtle()
line.speed(1)
line.showturtle()
line.color("black")
line.penup()
line.pensize(10)
line.goto(0,25)
line.pendown()
line.right(90)
line.forward(200)

line.penup()
line.goto(0,25)
line.pendown()
line.goto(50,50)

pond.exitonclick()



