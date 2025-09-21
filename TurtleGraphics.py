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
var MAX_SIZE = 120;
var MAX_SHAPES = 100;
var counter = 0;

function start(){
    setTimer(draw, 50);
}

function draw(){
    drawSquareWithCornerFill(Randomizer.nextInt(40, MAX_SIZE),
                             Randomizer.nextColor(),
                             Randomizer.nextInt(0, getWidth()),
                             Randomizer.nextInt(0, getHeight()),
                             Randomizer.nextInt(1, 4)); 
    
    counter++;
    if(counter == MAX_SHAPES){
        stopTimer(draw);
    }
}

function drawSquareWithCornerFill(size, color, cx, cy, corner){
    var rect = new Rectangle(size, size);
    rect.setColor(color);
    rect.setPosition(cx - size/2, cy - size/2);
    add(rect);

    var tri = new Polygon();
    if(corner === 1){ 
        tri.addPoint(cx - size/2, cy - size/2);
        tri.addPoint(cx, cy - size/2);
        tri.addPoint(cx - size/2, cy);
    } else if(corner === 2){ 
        tri.addPoint(cx, cy - size/2);
        tri.addPoint(cx + size/2, cy - size/2);
        tri.addPoint(cx + size/2, cy);
    } else if(corner === 3){ 
        tri.addPoint(cx - size/2, cy);
        tri.addPoint(cx, cy);
        tri.addPoint(cx - size/2, cy + size/2);
    } else { 
        tri.addPoint(cx, cy);
        tri.addPoint(cx + size/2, cy);
        tri.addPoint(cx + size/2, cy + size/2);
    }
    tri.setColor(Color.black); 
    add(tri);
}

#======================================================
#random square in squares


