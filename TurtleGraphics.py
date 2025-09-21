#TurtleGraphics.py
#Name: Pierce Limbo
#Date: 9/22/2025
#Assignment: Lab3 

#=======================
#Random Polygons
var MAX_SIZE = 80;
var MAX_SHAPES = 100;
var counter = 0;

function start(){
    setTimer(draw, 50);
}

function draw(){
    drawPolygon(Randomizer.nextInt(3, 8),     // random sides (triangle–octagon)
                Randomizer.nextInt(20, MAX_SIZE), 
                Randomizer.nextColor(),
                Randomizer.nextInt(0, getWidth()),
                Randomizer.nextInt(0, getHeight()));
    
    counter++;
    if(counter == MAX_SHAPES){
        stopTimer(draw);
    }
}

function drawPolygon(sides, radius, color, cx, cy){
    var poly = new Polygon();
    for(var i = 0; i < sides; i++){
        var ang = i * (2 * Math.PI / sides);
        var x = cx + radius * Math.cos(ang);
        var y = cy + radius * Math.sin(ang);
        poly.addPoint(x, y);
    }
    poly.setColor(color);
    add(poly);
}
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


