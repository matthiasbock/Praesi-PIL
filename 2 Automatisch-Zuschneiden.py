#!/usr/bin/python
#
# Automatisches Zuschneiden
#

from PIL import Image

# Parameter
transparent = (255,255,255,0)
bgcolor = transparent

# Bild laden
img = Image.open("tux.png")
pixels = img.load()

width = img.size[0]
height = img.size[1]

# Ausgangswerte fuer unseren Grenzfindungs-Algorithmus
minX = width
maxX = 0
minY = height
maxY = 0

# alle Zeilen durchgehen
for y in range(height):

    # alle Spalten durchgehen
    for x in range(width):

        # gehoert das Pixel zum Hintergrund ?
        if pixels[x,y][3] > 0:

            # die Grenzen unserer Zuschneide-Box ggf. anpassen
            if (x < minX):
                minX = x
            if (x > maxX):
                maxX = x
            if (y < minY):
                minY = y
            if (y > maxY):
                maxY = y

# mit den oben bestimmten Werten zuschneiden
img = img.crop( (minX,minY,maxX,maxY) )

# speichern
img.save("tux-cropped.png")
