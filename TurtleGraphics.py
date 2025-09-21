#TurtleGraphics.py
#Name: Pierce Limbo
#Date: 9/22/2025
#Assignment: Lab 4 

#=======================
#Random Polygons
import turtle
import random

def drawPolygon(myTurtle, sides, size=100):
    angle = 360 / sides
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(3)


    sides = random.randint(3, 10)
    drawPolygon(myTurtle, sides, 70)

    turtle.done()

if __name__ == "__main__":
    main()

#===========================================
#random corner
import turtle

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def fillCorner(myTurtle, corner):
    size = 200
    myTurtle.penup()
    myTurtle.goto(-size/2, size/2)  
    myTurtle.pendown()
    drawSquare(myTurtle, size)


    myTurtle.penup()
    if corner == 1:      
        myTurtle.goto(-size/2, 0)
    elif corner == 2:    
        myTurtle.goto(0, 0)
    elif corner == 3:    
        myTurtle.goto(-size/2, -size/2)
    elif corner == 4:  
        myTurtle.goto(0, -size/2)
    myTurtle.pendown()


    myTurtle.begin_fill()
    drawSquare(myTurtle, size/2)
    myTurtle.end_fill()

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(3)
    fillCorner(myTurtle, 2) 
    turtle.done()

if __name__ == "__main__":
    main()

#======================================================
#random square in squares
import turtle

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def squaresInSquares(myTurtle, num):
    size = 50
    for i in range(num):
        myTurtle.penup()
        myTurtle.goto(-size/2, size/2)  
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size += 50   

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(3)
    squaresInSquares(myTurtle, 5)
    turtle.done()

if __name__ == "__main__":
    main()


