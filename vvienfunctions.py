import turtle

bob = turtle.Turtle ()
turtle.colormode (255)

def jump (x, y):
    bob.penup ()
    bob.goto (x, y)
    bob.pendown ()

def illusion (size, color):
    bob.color (color)
    bob.width (2)
    for times in range (360):
        bob.circle (size)
        bob.left (80 + times * 45)

def polygon_nofill (sides, distance, c):
    bob.color (c)
    angle = 360/ sides
    for times in range (sides):
        bob.forward (distance)
        bob.left (angle)

def polygon_fill (sides, distance, c):
    bob.color (c)
    angle = 360/ sides
    bob.begin_fill ()
    for times in range (sides):
        bob.forward (distance)
        bob.left (angle)
    bob.end_fill()

def ninjastar_outline (distance, color):
    bob.width (2)
    for times in range (25):
        bob.right (45)
        polygon_nofill (3, 150, color)
        bob.left (120)
        bob.forward (distance)
        
def ninjastar (distance, color):
    for times in range (25):
        bob.right (45)
        polygon_fill (3, 150, color)
        bob.left (120)
        bob.forward (distance)

def opposite_ninjastar (distance, color):
    for times in range (25):
        bob.left (45)
        polygon_fill (3, 150, color)
        bob.right (120)
        bob.forward (distance)

def opposite_ninjastar_outline (distance, color):
    bob.width (2)
    for times in range (25):
        bob.left (45)
        polygon_nofill (3, 150, color)
        bob.right (120)
        bob.forward (distance)

def star (distance):
    bob.color ("yellow")
    bob.begin_fill()
    for times in range (15):
        bob.forward (distance)
        bob.left (120)
        bob.forward (distance)
        bob.right (90)
    bob.end_fill()

def star_outline (distance, color):
    bob.color (color)
    for times in range (15):
        bob.forward (distance)
        bob.left (120)
        bob.forward (distance)
        bob.right (90)
