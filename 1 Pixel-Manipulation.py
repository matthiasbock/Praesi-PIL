#!/usr/bin/python
#
# Wir zeichnen ein farbiges Bild mit PIL
#

from PIL import Image, ImageColor
from math import sin, pi

# gewuenschte Bildgroesse
width = 400
height = 500

# unsere Konstanten
white = ImageColor.getrgb("#FFFFFF")

# neues Bild erzeugen
art = Image.new("RGB", (width,height), white)

#
# Farben zuweisen
#

# expandiert Sinuswerte von [-1 bis 1] auf [0 bis 255]
def color_sine(angle):
    return (int) (( sin(angle*pi/180)+1 )*127)

# gibt abhaengig von der Koordinate eine Farbe zurueck
def my_color(x, y):
    return (
            color_sine(x),
            color_sine(y),
            color_sine(x+y)
            )

# zeichnet auf jede Koordinate unsere Wunschfarbe
for y in range(height):
    for x in range(width):
        art.putpixel( (x,y), my_color(x,y) )

# der Welt unser Kunstwerk zeigen
art.show()

# Kunstwerk fuer die Nachwelt konservieren
art.save("art.png")
