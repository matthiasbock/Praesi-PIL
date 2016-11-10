#!/usr/bin/python

from PIL import Image, ImageColor
from math import sin, pi

# Parameter
width = 400
height = 500

# Konstanten
white = ImageColor.getrgb("#FFFFFF")

# neues Bild
art = Image.new("RGB", (width,height), white)

# Farben zuweisen

def color_sine(angle):
    return (int) (( sin(angle*pi/180)+1 )*127)

def my_color(x, y):
    return (
            color_sine(x),
            color_sine(y),
            color_sine(x+y)
            )

for y in range(height):
    for x in range(width):
        art.putpixel( (x,y), my_color(x,y) )

# der Welt unser Kunstwerk zeigen
art.show()

# Kunstwerk fuer die Nachwelt konservieren
art.save("art.png")
