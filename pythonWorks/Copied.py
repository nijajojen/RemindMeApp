from turtle import *
from random import *

import math
def shooter_clicked(clickx,clicky): 
    global start
    start=True
    return
    
setup(600,500)
maxx = 300
maxy = 250
minx= -maxx
miny= - maxy
title ("shooting ball")
bgcolor('grey')
ball=Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(3,3,3)
ball.color("blue")
bounce_point = 20
shooter=Turtle()
shooter.hideturtle()
shooter.penup()
shooter.shape("square")
shooter.shapesize(3,3,3)
shooter.color("red")
shooter.goto(-10,-220)
bullet=Turtle()
bullet.hideturtle()
bullet.penup()
bullet.shape("circle")
bullet.shapesize(1,1,1)
bullet.goto(-20,-100)
shooter.onclick(shooter_clicked)
x = randint(minx + bounce_point, maxx + bounce_point)
y = randint(miny + bounce_point, maxy + bounce_point)
ball.goto(x,y)
ball.showturtle()
bullet.showturtle()
shooter.showturtle()
dx = 10
dy = 10
bdy=30
by=-140
endloop = False
start=False
while not endloop:
    
    
    xx = x + dx
    if xx < minx+bounce_point:
        xx = minx + bounce_point
        dx = -dx
        
    if xx > maxx - bounce_point:
        xx = maxx- bounce_point
        dx = -dx
        
    yy=y+dy
    if yy < miny + bounce_point: 
        yy= miny + bounce_point
        dy = -dy
        
    if yy > maxy + bounce_point:   
        yy = maxy + bounce_point
        dy = -dy
        
    x = xx
    y = yy
    ball.goto(x,y)
  
    
    shooter.goto(-by,-bdy)
    if start==True:
        by=by+bdy
        if by>maxy:
            by=-220
            start= False
            
        if bullet.distance(ball)<40:
            print ("target affirmed")
            print ("You win!!!!!!")
            endloop=True
            start=False
        bullet.goto(0,by)
    
    
                       
bye()