#										Bar Chart
#									-----------------
#This program will draw the performance chart of students against year.
#A data file need to be passed to the program to draw the chart.
#A data for a year is encapsulated into YearPerformance Object and used to draw the graph
#Developer : Nija Jojen
#Student ID: 90947

import sys
import turtle

#Global Data
studentsYear=[]
xTurtle=turtle.Turtle()
xTurtle.hideturtle()
yTurtle=turtle.Turtle()
yTurtle.hideturtle()
yNoPassTurtle=turtle.Turtle()
yNoPassTurtle.hideturtle()
yNoFailTurtle=turtle.Turtle()
yNoFailTurtle.hideturtle()

#Main Program
def main():
	if(len(sys.argv) != 2):
		print("Use Graph.py <filePath>")
		sys.exit()
	file_name = sys.argv[1]
	pond=initScreen()
	readData(file_name)
	drawBar()
	drawInfo("green","Students Passed",200)
	drawInfo("red","Students Failed", 150)
	destroy(pond)
	
#Initialize Screen
def initScreen():
	pond = turtle.Screen()
	turtle.setup (2000, 1000, 0, 0)
	pond.bgcolor("white")
	turtle.title ('Students Performance Report')
	return pond

#Destroy Screen
def destroy(pond):
	pond.exitonclick()

#Draw information bar
def drawInfo(color, text, y):
	plotTurtle = turtle
	turtle.color(color)
	turtle.fillcolor(color)
	plotTurtle.penup()
	plotTurtle.goto(200,y)
	plotTurtle.pendown()
	plotTurtle.begin_fill()
	plotTurtle.left(90)
	plotTurtle.forward(50)
	plotTurtle.right(90)
	plotTurtle.forward(50)
	plotTurtle.right(90)
	plotTurtle.forward(50)
	plotTurtle.right(90)
	plotTurtle.forward(50)
	plotTurtle.end_fill()
	plotTurtle.penup()
	plotTurtle.right(180)
	plotTurtle.penup()
	plotTurtle.goto(350,y)
	turtle.color("black")
	plotTurtle.write(text,False,"center",font=('Times New Roman', 12, 'bold'))


#Read Data from File
def readData(file_name):
	try:
		file = open(file_name,"r")
		for line in file:
			words=line.split()
			studentPerYear = YearPerformance(words[0],words[1],words[2],words[3])
			studentsYear.append(studentPerYear)	
		file.close()
	except IOError:
		print ("IOError")
		sys.exit()
	
#Draw Bar Chart
def drawBar():
	turtle.penup()
	turtle.hideturtle()
	xAxis=-600
	yAxis=-200
	turtle.goto(xAxis,yAxis)
	turtle.color("green")
	turtle.fillcolor("green")
	failTurtle=turtle.Turtle()
	failTurtle.hideturtle()
	failTurtle.penup()
	failTurtle.goto(xAxis + 50,yAxis)
	failTurtle.color("red")
	failTurtle.fillcolor("red")
	drawAxis(xTurtle, False)
	drawAxis(yTurtle, True)
	yNoPassTurtle.hideturtle()
	yNoFailTurtle.hideturtle()

	for i in range(len(studentsYear)):
		studenPerYear = studentsYear[i]
		passNo=int(studenPerYear.passNum)*5
		failNo=int(studenPerYear.failNum)*5
		graphPlot(turtle,passNo,i,yNoPassTurtle,False, studenPerYear)
		graphPlot(failTurtle,failNo,i,yNoFailTurtle,True,studenPerYear)
		xAxis=xAxis+150
		turtle.goto(xAxis,yAxis)
		failTurtle.goto(xAxis+50,yAxis)
		

#Plot Graph
def graphPlot(plotTurtle,height,j,x,isFail,studenPerYear):
	plotTurtle.pendown()
	plotTurtle.begin_fill()
	plotTurtle.left(90)
	plotTurtle.forward(height)
	positn=plotTurtle.position()
	x.penup()
	x.goto(positn[0]+25,positn[1])
	if isFail==False:
		
		x.write(studenPerYear.passNum,False,"center",font=('Times New Roman', 12, 'bold'))
	
	else:
		x.write(studenPerYear.failNum,False,"center",font=('Times New Roman', 12, 'bold'))


	plotTurtle.right(90)
	plotTurtle.forward(50)
	plotTurtle.right(90)
	plotTurtle.forward(height)


	plotTurtle.right(90)
	plotTurtle.forward(50)
	plotTurtle.end_fill()
	plotTurtle.penup()
	plotTurtle.right(180)
	

# Draw Axis
def drawAxis(axisTurtle, isY):
	axisTurtle.hideturtle()
	if isY:
		axisTurtle.left(90)
		tempLen=400
	else:
		tempLen=800

	axisTurtle.penup()
	axisTurtle.goto(-600,-200)
	axisTurtle.pendown()
	axisTurtle.showturtle()
	axisTurtle.forward(tempLen)

	if isY==False:
		yearTurtle=turtle.Turtle()
		yearTurtle.hideturtle()
		xPointYr=-570
		yearTurtle.penup()
		yearTurtle.goto(xPointYr,-220)
		yearTurtle.color="black"
		#yearTurtle.showturtle()
		for i in range(len(studentsYear)):
			studenPerYear = studentsYear[i]
			yearTurtle.write(studenPerYear.year,False,font=('Times New Roman', 12, 'bold'))
			xPointYr=xPointYr+150
			yearTurtle.goto(xPointYr,-220)

class YearPerformance:
   
   def __init__(self, year, numStudents, passNum, failNum):
      self.year = year
      self.passNum = passNum
      self.failNum = failNum
      self.numStudents = numStudents
      
		
main()
