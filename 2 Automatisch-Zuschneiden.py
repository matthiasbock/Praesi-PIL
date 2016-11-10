#!/usr/bin/python
#
# Automatisches Zuschneiden
#

from PIL import Image

# Hintergrundfarbe: weiss
bgcolor = (255,255,255)

# Bild laden
tux = Image.load("tux.png")

# Kleinestes Rechteck mit Nicht-Null-Pixeln bestimmen ("Bounding Box")
bbox = tux.getbbox()

print bbox
# sicherlich falsche Ausgangswerte
minX = width
maxX = 0
minY = height
maxY = 0

# alle Zeilen durchgehen
for y in range(height):

    # alle Spalten durchgehen
    for x in range(width):

        # dieses Pixels gehoert nicht zum Hintergrund
        if pixel[x,y] != bgcolor:

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
img.crop(minX, minY, maxX, maxY)

# speichern

img.save("Zugeschnitten.jpg")
