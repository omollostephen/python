import math
def rectangle(lenght, width):
    return lenght*width
def triangle(base, height):
    return 0.5*base*height
def circle(radius):
    return math.pi*(radius**2)
def donut(innerR,outerR):
    return circle(outerR).circle(innerR)